import curses
import datetime
import random

def times(key_times):
	return [t.seconds + t.microseconds / 1000000.0 for _, _, t in key_times]

def mean(key_times):
	ts = times(key_times)
	return sum(ts) / len(ts)

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(2)
curses.noecho()

sentences = []
with open('sentences.txt') as sentence_file:
	for line in sentence_file:
		sentences.append(line)

finished = False
while not finished:
	sentence = random.choice(sentences)
	key_log = []
	stdscr.addstr(sentence)
	y, x = curses.getsyx()
	for letter in sentence:
		stdscr.refresh()
		lt, t = None, datetime.datetime.now()
		c = None

		while c != ord(letter):
			c = stdscr.getch()
			lt, t = t, datetime.datetime.now()
			if c == ord('^'):
				finished = True
				break
			if lt:
				key_log.append((letter, chr(c), t - lt))
			if c != ord(letter):
				curses.beep()
		y, x = curses.getsyx()
		stdscr.move(y, x+1)
	stdscr.addstr(str(mean(key_log)))
	y, x = curses.getsyx()
	stdscr.move(y+1, 0)

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

for t in key_log:
	print(t)

ts = times(key_log)

print("\n, min: {0}, max: {1}, mean: {2}".format(min(ts), max(ts), mean(ts)))
