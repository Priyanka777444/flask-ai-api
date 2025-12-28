from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello, this is me Priyanka Late",
        "status": "running",
        "creator": "It's me Ms. Priyanka"
    })

# AI prediction endpoint (dummy for now)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')

    return jsonify({
        "input": text,
        "prediction": "positive",
        "confidence": 0.92,
        "message": "Dummy demo of API by Priyanka"
    })

# About endpoint
@app.route('/about')
def about():
    return jsonify({
        "name": "Priyanka Late",
        "role": "AI/ML Developer",
        "skills": ["Python", "Flask", "Machine Learning", "GenAI"]
    })

if __name__ == "__main__":
    app.run(debug=True)
