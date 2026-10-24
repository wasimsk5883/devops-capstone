
from flask import Flask, jsonify

app = Flask(__name__)

cart = [
    {"product_id": 1, "name": "Laptop", "quantity": 1},
    {"product_id": 2, "name": "Keyboard", "quantity": 2}
]

@app.route("/")
def home():
    return jsonify({"message": "Cart Service is running!"})

@app.route("/cart")
def get_cart():
    return jsonify(cart)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
