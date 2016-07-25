from collections import defaultdict
import os.path
import pickle

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
	
	model[0] = list(model.keys())
	model.seeds = model[0]

	return model

def english_model():
	if os.path.isfile('.english_model.p'):
		with open('.english_model.p', 'rb') as pickle_file:
			model = pickle.load(pickle_file)
			model.seeds = model[0]
			return model
	model = _build_model()
	with open('.english_model.p', 'wb') as pickle_file:
		pickle.dump(model, pickle_file)
	return model