from collections import Counter
from flask import jsonify


def process_word(pyramid_word):
	if pyramid_word.isalpha():
		_letter_data = list(Counter(pyramid_word.lower()).items())
		ordered_letters = sorted(_letter_data, key=lambda x: x[1])
		if ordered_letters[0][1] != 1 or len(ordered_letters) == 1:
			return build_resp("NOT A PYRAMID: Word only contains one unique letter", 200)
		for i in range(len(ordered_letters)):
			try:
				if ordered_letters[i][1]+1 == ordered_letters[i+1][1]:
					continue
				else:
					return build_resp(
						"NOT A PYRAMID: The word passed is not a pyramid word:'{}'. Word pyramid output: {}".format(
							pyramid_word, ordered_letters), 200
					)
			except IndexError:
				return build_resp("PYRAMID FOUND: The word passed is a pyramid word: '{}'. Word pyramid output: {}".format(
					pyramid_word, ordered_letters), 200
				)
	else:
		return build_resp(
			"Unable to process: Word contains numbers or special chars. Word {}".format(pyramid_word), 400
		)


def build_resp(resp_data, status_code):
	return jsonify(
		response=resp_data,
		status=status_code
	)