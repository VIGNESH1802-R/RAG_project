from flask import Flask, request, jsonify
from flask_cors import CORS

from QueryProcessor import process_user_query

app = Flask(__name__)

CORS(app)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data.get("question")

    answer = process_user_query(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":

    app.run(debug=True)