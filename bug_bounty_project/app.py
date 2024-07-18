from flask import Flask, render_template, request, jsonify

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
    input_data = request.form.get('input')
    result = {"message": f"Subdomain finder for {input_data}"}
    return jsonify(result)

@app.route('/api/directory_scanner', methods=['POST'])
def api_directory_scanner():
    input_data = request.form.get('input')
    result = {"message": f"Directory scanner for {input_data}"}
    return jsonify(result)

@app.route('/api/port_scanner', methods=['POST'])
def api_port_scanner():
    input_data = request.form.get('input')
    result = {"message": f"Port scanner for {input_data}"}
    return jsonify(result)

@app.route('/api/vulnerability_scanner', methods=['POST'])
def api_vulnerability_scanner():
    input_data = request.form.get('input')
    result = {"message": f"Vulnerability scanner for {input_data}"}
    return jsonify(result)

@app.route('/api/http_request_analyzer', methods=['POST'])
def api_http_request_analyzer():
    input_data = request.form.get('input')
    result = {"message": f"HTTP request analyzer for {input_data}"}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
