from flask import Flask, request, jsonify
import os
from openai import AzureOpenAI

app = Flask(__name__)

# Load environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Initialize AzureOpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-07-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Call Azure OpenAI API using AzureOpenAI client
        response = client.completions.create(
            deployment_id=AZURE_OPENAI_DEPLOYMENT_NAME,
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the response text
        response_text = response["choices"][0]["text"].strip()

        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
