from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

# Flask App Setup
app = Flask(__name__)
CORS(app)

# Configuration
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "32281cfb-4cc4-4c77-b716-cc9848a326cf"
FLOW_ID = "97e6b247-d6c6-43a3-b5ca-e8aa6e886f91"
APPLICATION_TOKEN = "AstraCS:wlYoHfnOyOkqZLnWUHPqaEhl:72141966a6dbfca1db71fa0a391e2d9e1305988817a00879146a7ccfa7a722c0"
ENDPOINT = "research"

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot API Route
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    try:
        data = request.json
        message = data.get("message", "")

        response = requests.post(
            f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}",
            json={"input_value": message, "output_type": "chat", "input_type": "chat"},
            headers={"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}
        )

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
