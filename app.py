from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

app = Flask(__name__)

CUSTOM_ENDPOINT = os.getenv("CUSTOM_ENDPOINT")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

@app.route('/v1/engines/chat/completions', methods=['POST'])
def handle_request():
    data = request.json
    prompt = data.get("prompt")
    temperature = data.get("temperature")
    max_tokens = data.get("max_tokens")

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "prompt": prompt
    }

    pprint(payload)

    #response = requests.post(CUSTOM_ENDPOINT, json=payload)
    #return jsonify(response.json())
    response = {"reply": "Hello, World!"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
