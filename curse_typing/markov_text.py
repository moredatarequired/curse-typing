import random

import text_model

def random_word(words, model):
	key = tuple(words[-4:])
	while key not in model:
		if len(key) <= 1:
			return None
		key = key[1:]
	options = model[key]
	total = sum(c for _, c in options)
	choice = random.randrange(0, total)
	for word, p in options:
		choice -= p
		if choice <= 0:
			return word
	assert(False)

def random_sentence(model, length=60):
	words = list(random.choice(model.seeds))
	while sum(len(w) for w in words) < length:
		next = random_word(words, model)
		if next is None:
			return random_sentence(model, length)
		words.append(next)
	return ' '.join(words[:-1])

def english_nonsense():
	return random_sentence(text_model.english_model(), 80)
