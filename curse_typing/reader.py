
from pathlib import Path

SOURCE = 'untyped.txt'

with open(SOURCE) as infile:
    book = infile.readlines()

def line_to_sentences(line):
    words = line.split()
    next_part = []
    while words:
        if len(words[0]) + sum(len(s) for s in next_part) < 80:
            next_part.append(words[0])
            words = words[1:]
        else:
            yield ' '.join(next_part)
            next_part = []
    if next_part:
        yield ' '.join(next_part)

sentences = []
for line in book:
    sentences.extend(line_to_sentences(line.strip()))

with open('sentences-cory.txt', 'w') as outfile:
    for sentence in sentences:
        outfile.write(f'{sentence}\n')
