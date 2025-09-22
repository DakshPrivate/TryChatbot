from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simple mock NLP chatbot
def simple_bot(message):
    responses = [
        "That’s interesting, tell me more.",
        "Why do you think that?",
        "I see, go on...",
        "Hmm, good point!",
        "Let me think about that..."
    ]
    return random.choice(responses)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = simple_bot(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
