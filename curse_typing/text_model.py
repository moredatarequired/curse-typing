from collections import defaultdict
import os.path
import pickle

ENGLISH_NGRAM_FILES = ['w5.txt', 'w4.txt', 'w3.txt', 'w2.txt']

class TextModel(defaultdict):
	pass

def _ngram_line(line):
	'Get the count, prefix and final word of an ngram line.'
	parts = line.split()
	if parts[1] == "n't":
		parts[1:] = parts[2:]
	for i in range(2, len(parts)-1):
		if parts[i+1] == "n't":
			parts[i] = parts[i] + parts[i+1]
			parts[i+1:] = parts[i+2:]
			break
	return int(parts[0]), tuple(parts[1:-1]), parts[-1]

def _build_model():
	model = TextModel(list)

	for ngram_file in ENGLISH_NGRAM_FILES:
		with open(ngram_file) as infile:
			for line in infile:
				count, key, word = _ngram_line(line)
				model[key].append((word, count))
	
	model[0] = list(model.keys())
	model.seeds = model[0]

	return model

model = None
def english_model():
	global model
	if model:
		return model
	if os.path.isfile('.english_model.p'):
		with open('.english_model.p', 'rb') as pickle_file:
			model = pickle.load(pickle_file)
			model.seeds = model[0]
			return model
	model = _build_model()
	with open('.english_model.p', 'wb') as pickle_file:
		pickle.dump(model, pickle_file)
	return model