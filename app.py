
import requests
from flask import Flask, jsonify, request
from github_search import best_project_online_search
from openai_call import best_project_offline_model

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/bestprojects', methods=['GET'])
def get_best_project():
    need = request.args.get('need')
    mode = request.args.get('mode')
    if mode=='offline':
        projects = best_project_offline_model(need)
    else:
        projects = best_project_online_search(need)
    return jsonify(projects)


if __name__ == "__main__":
    app.run(port=8080)
