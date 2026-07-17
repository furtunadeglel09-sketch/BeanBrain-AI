from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to BeanBrain AI",
        "status": "Running"
    })

@app.route("/analyze")
def analyze():
    return jsonify({
        "success_score": 85,
        "risk_level": "Low",
        "recommendations": [
            "Offer specialty coffee",
            "Create loyalty program",
            "Analyze local customers"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
