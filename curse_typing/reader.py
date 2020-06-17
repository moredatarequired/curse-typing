
from pathlib import Path

SOURCE = 'untyped.txt'


def line_to_sentences(line):
    words = line.split()
    next_part = ''
    while words:
        if len(words[0]) + len(next_part) >= 80:
            yield next_part
            next_part = ''
        else:
            next_part = f"{next_part} {words[0]}"
            words = words[1:]
    if next_part:
        yield next_part

def create_sentences():
    with open(SOURCE) as infile:
        book = infile.readlines()

    sentences = []
    for line in book:
        sentences.extend(line_to_sentences(line.strip()))

    with open('sentences-cory.txt', 'w') as outfile:
        for sentence in sentences:
            outfile.write(f'{sentence}\n')


def sentence_generator():
    with open('sentences-cory.txt') as infile:
        for sentence in infile:
            yield sentence


if __name__ == "__main__":
    create_sentences()