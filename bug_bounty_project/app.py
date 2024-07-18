from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subdomain_finder')
def subdomain_finder():
    return render_template('subdomain_finder.html')

@app.route('/directory_scanner')
def directory_scanner():
    return render_template('directory_scanner.html')

@app.route('/port_scanner')
def port_scanner():
    return render_template('port_scanner.html')

@app.route('/vulnerability_scanner')
def vulnerability_scanner():
    return render_template('vulnerability_scanner.html')

@app.route('/http_request_analyzer')
def http_request_analyzer():
    return render_template('http_request_analyzer.html')

@app.route('/api/subdomain_finder', methods=['POST'])
def api_subdomain_finder():
    input_data = request.json.get('domain')
    github_token = os.getenv('GITHUB_TOKEN')
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    workflow_url = 'https://api.github.com/repos/Joker-992001/Tools/actions/workflows/subdomain_enum.yml/dispatches'
    data = {
        "ref": "main",
        "inputs": {
            "domain": input_data
        }
    }
    
    response = requests.post(workflow_url, json=data, headers=headers)
    
    if response.status_code == 204:
        time.sleep(10)  # Wait for the workflow to complete
        results_url = 'https://raw.githubusercontent.com/Joker-992001/Tools/main/public/results/alive_subdomains.txt'
        results_response = requests.get(results_url)
        if results_response.status_code == 200:
            results = results_response.text
            return jsonify({"message": f"Subdomain enumeration results for {input_data}", "results": results})
        else:
            return jsonify({"message": "Failed to fetch results"}), 500
    else:
        return jsonify({"message": "Failed to trigger workflow"}), 500

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
