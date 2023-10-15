from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def post_example():
    # Get JSON data
    data = request.get_json()

    # Check if "message" key exists in JSON and it's not empty
    if 'message' in data and data['message']:
        print(f"Message received: {data['message']}")
        return jsonify(success=True, message="Data received"), 200
    else:
        return jsonify(success=False, message="No message provided"), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)