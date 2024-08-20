from flask import Blueprint, request, jsonify
from .vertex_ai_client import send_prompt_to_vertex

main = Blueprint('main', _name_)

@main.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = send_prompt_to_vertex(prompt)
    return jsonify({"response": response})