from collections import Counter, OrderedDict


def get(pyramid_word):
	# import pdb;pdb.set_trace()
	_letter_data = list(Counter(pyramid_word).items())
	ordered_letters = sorted(_letter_data, key=lambda x: x[1])
	for i in range(len(ordered_letters)-1):
		try:
			if ordered_letters[i][1]+1 == ordered_letters[i+1][1]:
				continue
			else:
				return "The word passed is not a pyramid word: '{}'. Word Output: {}".format(pyramid_word, ordered_letters)
		except KeyError:
			return "PYRAMID FOUND: The word passed is a pyramid word: '{}'. Word Output: {}".format(pyramid_word, ordered_letters)


	
	