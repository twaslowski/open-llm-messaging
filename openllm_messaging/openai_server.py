import logging
import os

from flask import Flask, jsonify, request

from openllm_messaging.llm.openai.openai_adapter import OpenAIAdapter

app = Flask(__name__)
key = os.getenv("OPENAI_API_KEY")
openai_adapter = OpenAIAdapter(key)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@app.route("/text", methods=["POST"])
def text():
    prompt = request.json.get("prompt")
    logging.info("Received prompt: %s", prompt)
    openai_response = openai_adapter.chat_completion_simple(prompt)
    logging.info("Responding with: %s", openai_response)
    return jsonify(openai_response.as_dict())


@app.route("/image", methods=["POST"])
def image():
    return "Not implemented", 501


def run():
    app.run(host="0.0.0.0", port=5001)
