#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Sublist3r
install_sublist3r() {
    echo "Installing Sublist3r..."
    git clone https://github.com/aboul3la/Sublist3r.git
    cd Sublist3r || exit
    sudo pip3 install -r requirements.txt
    cd ..
    sudo ln -s "$(pwd)"/Sublist3r/sublist3r.py /usr/local/bin/sublist3r
}

# Function to install subfinder
install_subfinder() {
    echo "Installing subfinder..."
    GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
    export PATH=$PATH:$(go env GOPATH)/bin
}

# Function to install httpx
install_httpx() {
    echo "Installing httpx..."
    GO111MODULE=on go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
    export PATH=$PATH:$(go env GOPATH)/bin
}

# Install dependencies if needed
if [ "$1" == "--install-dependencies" ]; then
    # Check if Sublist3r is installed, install if not
    if ! command_exists sublist3r; then
        install_sublist3r
    fi

    # Check if subfinder is installed, install if not
    if ! command_exists subfinder; then
        install_subfinder
    fi

    # Check if httpx is installed, install if not
    if ! command_exists httpx; then
        install_httpx
    fi

    exit 0
fi

# Ensure the domain is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

DOMAIN=$1
OUTPUT_DIR="output"
SUBDOMAINS_FILE="$OUTPUT_DIR/subdomains.txt"
ALIVE_SUBDOMAINS_FILE="$OUTPUT_DIR/alive_subdomains.txt"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Enumerate subdomains with Sublist3r
echo "[*] Enumerating subdomains with Sublist3r..."
sublist3r -d "$DOMAIN" -o "$OUTPUT_DIR/sublist3r.txt"

# Enumerate subdomains with subfinder
echo "[*] Enumerating subdomains with subfinder..."
subfinder -d "$DOMAIN" -o "$OUTPUT_DIR/subfinder.txt"

# Combine results
echo "[*] Combining results..."
cat "$OUTPUT_DIR/sublist3r.txt" "$OUTPUT_DIR/subfinder.txt" | sort -u >"$SUBDOMAINS_FILE"

# Check if subdomains are alive
echo "[*] Checking if subdomains are alive..."
httpx -l "$SUBDOMAINS_FILE" -silent -status-code -o "$ALIVE_SUBDOMAINS_FILE"

echo "[*] Done. Results saved in the $OUTPUT_DIR directory."
