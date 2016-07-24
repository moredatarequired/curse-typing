from collections import defaultdict

ENGLISH_NGRAM_FILES = ['w5.txt', 'w4.txt', 'w3.txt', 'w2.txt']

class TextModel(defaultdict):
	pass

def _build_model():
	model = TextModel(list)

	for ngram_file in ENGLISH_NGRAM_FILES:
		with open(ngram_file) as infile:
			for line in infile:
				parts = line.split()
				count, key, word = int(parts[0]), tuple(parts[1:-1]), parts[-1]
				model[key].append((word, count))
	
	model.seeds = list(model.keys())

	return model

def english_model():
	return _build_model()