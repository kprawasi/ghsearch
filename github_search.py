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



def best_project_online_search(need):
    projects = query_github_projects(need)
    #print(type(projects[12]))
    if not projects:
        return "No projects found for this need."
    projects = sorted(projects, key=lambda project: project['stargazers_count'], reverse=True)
    projects = [str(i+1)+". "+project['name']+" " for i, project in enumerate(projects)]
    consolidated_names = projects[0]+projects[1]+projects[2]
    print(consolidated_names)
    return {'name':consolidated_names}

if __name__ == "__main__":
    need = "Analytics"
    best_project = best_project_online_search(need)
    print(f"The best open source project for '{need}' is: {best_project}")

