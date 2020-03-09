import json
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest, BadGateway
try:
	from word_pyramid.word_pyramid import process_word
except ModuleNotFoundError:
	from .word_pyramid.word_pyramid import process_word

app = Flask(__name__)


def create_app(app):
	return app


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
	return render_template('form.html', message=None)


@app.route('/process_word')
def form_handler():
	if len(request.url.split('=')) > 2:
		raise BadRequest("Data passed incorrectly. Ensure you entered a word ONLY containingletters.")
	else:
		word = request.url.split('=')[-1]
		_resp = process_word(word)
		_msg = json.loads(_resp.data)['response']
		return render_template('form.html',message=_msg)


if __name__ == '__main__':
	app.run(debug=False, port=9090)