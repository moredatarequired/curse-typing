from markov_text import english_nonsense
import curses
from curses import wrapper
import time


def practice(stdscr):
    stdscr.clear()
    while True:
        practice_sentence(stdscr)


def practice_sentence(stdscr):
    sentence = english_nonsense()
    stdscr.addstr(sentence + "\n")

    done = False
    start = time.perf_counter()
    i = 0
    keystrokes = []

    while not done:
        c = stdscr.getkey()
        t = time.perf_counter() - start
        keystrokes.append((c, t))

        stdscr.addch(c)
        if c == sentence[i]:
            i += 1
            if i >= len(sentence):
                done = True
            y, x = curses.getsyx()
            stdscr.move(y, x + 1)
        stdscr.refresh()

    y, x = curses.getsyx()
    stdscr.move(y + 1, 0)
    stdscr.refresh()

    return sentence, keystrokes


if __name__ == "__main__":
    wrapper(practice)
