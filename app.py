from flask import Flask, request, jsonify
from word_pyramid.word_pyramid import process_word

app = Flask(__name__)


@app.route('/pyramid-word', methods=['GET'])
def word_handler():
    try:
        req = request.args.get('word')
        if req:
            resp = process_word(req)
            return resp
        else:
            #raise 400 error for improper data format
            return jsonify(
                response="Data passed incorrectly. Ensure you entered using the format '/pyramid-word?word=<your word>'"
            )
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(debug=True, port=9090)