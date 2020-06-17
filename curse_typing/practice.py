from string import printable
import curses
from curses import wrapper
import time

from reader import sentence_generator


def practice(stdscr):
    stdscr.clear()
    for sentence in sentence_generator():
        practice_sentence(stdscr, sentence)


def practice_sentence(stdscr, sentence):
    sentence = "".join(c for c in sentence.strip() if c in printable)
    y, x = curses.getsyx()
    stdscr.addstr(sentence + "\n")
    stdscr.move(y, x)

    done = False
    start = None
    i = 0
    keystrokes = []

    while not done:
        c = stdscr.getkey()
        if start is None:
            start = time.perf_counter()
        t = time.perf_counter() - start
        keystrokes.append((c, t))

        if c == sentence[i]:
            i += 1
            stdscr.move(y, x + i)
            if i >= len(sentence):
                done = True
        stdscr.refresh()

    avg = keystrokes[-1][1] / len(sentence)
    mistakes = len(keystrokes) - len(sentence)
    stdscr.move(y, 80)
    stdscr.addstr(f"  # wrong: {mistakes}; speed: {avg}\n")

    y, x = curses.getsyx()
    stdscr.move(y + 1, 0)
    stdscr.refresh()

    return keystrokes


if __name__ == "__main__":
    wrapper(practice)
