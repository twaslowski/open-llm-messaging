import os

from flask import Flask, jsonify, request

from openllm_messaging.llm.openai.openai_adapter import OpenAIAdapter

app = Flask(__name__)
token = os.getenv("OPENAI_API_TOKEN")
openai_adapter = OpenAIAdapter(token)


@app.route("/text", methods=["POST"])
def text():
    prompt = request.json.get("prompt")
    openai_response = openai_adapter.chat_completion_simple(prompt)
    return jsonify(openai_response.as_dict())


@app.route("/image", methods=["POST"])
def image():
    return "Not implemented", 501


def run():
    app.run()
