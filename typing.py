import curses
import datetime

stdscr = curses.initscr()
curses.cbreak()
curses.echo()

t, lt = None, None

times = []

while True:
	c = stdscr.getch()
	lt, t = t, datetime.datetime.now()
	if c == ord('^'):
		break
	if lt:
		times.append(t - lt)

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

for t in times:
	print(t)

print("\n, min: {0}, max: {1}, mean: {2}".format(
	min(times), max(times), sum(times, datetime.timedelta())/len(times)))
