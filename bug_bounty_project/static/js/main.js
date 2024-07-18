// Main JavaScript file
console.log("Bug Bounty Tools website is running.");

// Subdomain Enum part

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('subdomain-form');
    const resultsDiv = document.getElementById('results');
    const subdomainList = document.getElementById('subdomain-list');
    const backButton = document.getElementById('backButton');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const domain = document.getElementById('domain').value;
        fetchSubdomains(domain);
    });

    backButton.addEventListener('click', function() {
        resultsDiv.classList.add('hidden');
        form.classList.remove('hidden');
    });

    function fetchSubdomains(domain) {
        fetch('/api/subdomain_finder', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ domain: domain })
        })
        .then(response => response.json())
        .then(data => {
            if (data.results) {
                displayResults(data.results.split('\n'));
            } else {
                displayResults([]);
            }
        })
        .catch(error => {
            console.error('Error fetching subdomains:', error);
        });
    }

    function displayResults(subdomains) {
        form.classList.add('hidden');
        resultsDiv.classList.remove('hidden');
        subdomainList.innerHTML = '';
        if (subdomains.length > 0) {
            subdomains.forEach(subdomain => {
                if (subdomain) {
                    const listItem = document.createElement('li');
                    listItem.textContent = subdomain;
                    subdomainList.appendChild(listItem);
                }
            });
        } else {
            subdomainList.innerHTML = '<li>No subdomains found.</li>';
        }
    }
});
