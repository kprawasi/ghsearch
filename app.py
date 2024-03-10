
import requests
from flask import Flask, jsonify, request
from search import find_best_project_for_need

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/bestprojects', methods=['GET'])
def get_best_project():
    need = request.args.get('need')
    best_project = find_best_project_for_need(need)
    return jsonify(best_project)

if __name__ == "__main__":
    app.run(port=8080)
