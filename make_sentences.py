from markov_text import english_nonsense

with open('sentences.txt', 'w') as outfile:
	for i in range(1000):
		outfile.write(english_nonsense() + '\n')
