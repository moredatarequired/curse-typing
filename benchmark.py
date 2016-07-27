import markov_text
import timeit

markov_text.english_nonsense()

print(timeit.repeat(
	stmt='markov_text.english_nonsense()',
	setup='import markov_text', repeat=5, number=1000))
# generating a nonsense sentence takes about 1ms on a puny macbook air