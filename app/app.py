from flask import Flask, request, jsonify
import os
from azure.identity import DefaultAzureCredential
from azure.ai.openai import OpenAIClient

app = Flask(__name__)

# Load environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Create OpenAI client
credential = DefaultAzureCredential()
openai_client = OpenAIClient(endpoint=AZURE_OPENAI_ENDPOINT, credential=credential)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Call Azure OpenAI API
        response = openai_client.get_completions(
            deployment_id=AZURE_OPENAI_DEPLOYMENT_NAME,
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the response text
        response_text = response.choices[0].text.strip()

        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)