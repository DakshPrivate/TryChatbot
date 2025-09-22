from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Simple mock NLP chatbot logic
def simple_bot(message: str) -> str:
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    elif "weather" in message:
        return "I can’t fetch live weather yet, but it’s always sunny in here ☀️"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        responses = [
            "That’s interesting, tell me more.",
            "Why do you think that?",
            "I see, go on...",
            "Hmm, good point!",
            "Let me think about that..."
        ]
        return random.choice(responses)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "NLP Chatbot API is running 🚀"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Please provide a 'message' field"}), 400
    
    user_message = data["message"]
    bot_response = simple_bot(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    # Important for Render (listens on 0.0.0.0:5000)
    app.run(host="0.0.0.0", port=5000)
