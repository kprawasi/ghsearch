
import yaml
import json
from openai import OpenAI
#import openai
# Set up your OpenAI API key here
with open('secrets.yml', 'r') as f:
    data = yaml.safe_load(f)
client = OpenAI(api_key=data['api_key'])
def complete_text(messages):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=json.loads(messages),
    temperature=0.2,
    max_tokens=256
    )
    return response.choices[0].message.content

def best_project_offline_model(need):
    prompt = "List three open source projects for " +need+". Be very crisp, just list the names"
    messages = json.dumps([{'role': 'user','content':prompt}])
    projects = complete_text(messages)
    return {'name':projects}



if __name__ == "__main__":
    prompt = "List three open source projects for web development. Be very crisp, just list the names"
    messages = json.dumps([{'role': 'user','content':prompt}])
    print(type(messages))
    print(type(json.loads(messages)))
    completion = complete_text(messages)
    print(completion)
