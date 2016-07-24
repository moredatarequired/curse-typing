from collections import defaultdict
import random

def build_model():
	model = defaultdict(list)

	with open('w5.txt') as infile:
		for line in infile:
			parts = line.split()
			count, key, word = int(parts[0]), tuple(parts[1:-1]), parts[-1]
			model[key].append((word, count))

	return model

def random_word(words, model):
	key = tuple(words[-4:])
	if key not in model:
		return None
	options = model[key]
	total = sum(c for _, c in options)
	choice = random.randrange(0, total)
	for word, p in options:
		choice -= p
		if choice <= 0:
			return word
	assert(False)

def random_sentence(model, length=10):
	words = list(random.choice(list(model.keys())))
	while len(words) < length:
		next = random_word(words, model)
		if next is None:
			break
		words.append(next)
	return ' '.join(words)

model = build_model()
for i in range(10):
	print(random_sentence(model))