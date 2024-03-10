# backend.py

import requests
import json
import yaml

with open('secrets.yml', 'r') as file:
    data = yaml.safe_load(file)
ghtoken ='Bearer '+data['ghtoken']
def query_github_projects(query):
    headers = {
        'Authorization': ghtoken,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        return []

def find_best_project_for_need(need):
    projects = query_github_projects(need)
    #print(type(projects[12]))
    if not projects:
        return "No projects found for this need."
    #print(projects[0].keys())
    best_project = max(projects, key=lambda project: project['stargazers_count'])
    return best_project

if __name__ == "__main__":
    need = "rag applications"
    best_project = find_best_project_for_need(need)
    print(f"The best open source project for '{need}' is: {best_project['html_url']}")

