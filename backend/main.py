from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/app/(root)/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello World"
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")