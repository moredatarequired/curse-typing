import random

import text_model

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
	words = list(random.choice(model.seeds))
	while len(words) < length:
		next = random_word(words, model)
		if next is None:
			break
		words.append(next)
	return ' '.join(words)

model = text_model.english_model()
for i in range(10):
	print(random_sentence(model))