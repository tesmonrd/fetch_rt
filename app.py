from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest, BadGateway
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
            raise BadRequest("Data passed incorrectly. Ensure you entered using the format '/pyramid-word?word=***'")
    except Exception as e:
        raise BadRequest("Encountered server error:{}".format(e))

@app.route('/')
def ui_option():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=9090)