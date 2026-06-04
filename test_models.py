import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)

print(response.status_code)
if response.status_code == 200:
    models = response.json().get('models', [])
    for m in models:
        print(m.get('name'))
else:
    print(response.text)
