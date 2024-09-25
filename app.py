import json
import os
from flask import Flask, jsonify, request, send_file, send_from_directory
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)

os.environ["GOOGLE_API_KEY"] = "AIzaSyCyywOiYIvjtQ08haIsIrpcgSDoEz80y_8"

# Serve the chatbot interface at the /chat route
@app.route('/chat')
def chat():
    return send_file('web/index.html')

# Defines a route for the /api/generate endpoint that accepts POST requests.
@app.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        try:
            req_body = request.get_json()
            content = req_body.get("contents")
            model = ChatGoogleGenerativeAI(model=req_body.get("model"))
            message = HumanMessage(content=content)
            response = model.stream([message])
            
            def stream():
                for chunk in response:
                    yield 'data: %s\n\n' % json.dumps({"text": chunk.content})

            return stream(), {'Content-Type': 'text/event-stream'}

        except Exception as e:
            return jsonify({"error": str(e)})

# Serve static files from the web directory
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('web', path)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
