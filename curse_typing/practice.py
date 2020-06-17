from string import printable
import curses
from curses import wrapper
import time
from collections import namedtuple
from datetime import datetime
import pickle

from reader import sentence_generator

HISTORY_FILE = ".history"

Keystroke = namedtuple("Keystroke", "intended actual timestamp")
Attempt = namedtuple("Attempt", "prompt timestamp keystrokes")


def previous_atempts():
    with open(HISTORY_FILE, "rb") as recfile:
        while True:
            try:
                yield pickle.load(recfile)
            except EOFError:
                break


def record(attempt):
    with open(HISTORY_FILE, "ab") as recfile:
        pickle.dump(attempt, recfile)


def practice(stdscr):
    past_prompts = set(a.prompt for a in previous_atempts())

    stdscr.clear()
    for sentence in sentence_generator():
        if sentence in past_prompts:
            continue
        attempt_ts = datetime.now()
        keystrokes = practice_sentence(stdscr, sentence)
        record(Attempt(sentence, attempt_ts, keystrokes))


def cpm(keystrokes):
    duration = keystrokes[-1].timestamp
    phraselen = sum(c == a for c, a, _ in keystrokes)
    return int(60 * (phraselen - 1) / duration) if duration else None


def mistakes(keystrokes):
    """Get the number of streaks of wrong keys."""
    streak = False
    wrong = 0
    for c, a, _ in keystrokes:
        if streak:
            if c == a:
                streak = False
            continue
        if c != a:
            streak = True
            wrong += 1

    return wrong


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
            if c != sentence[i]:
                continue
            start = time.perf_counter()
        t = time.perf_counter() - start
        keystrokes.append(Keystroke(sentence[i], c, t))

        if c == sentence[i]:
            i += 1
            stdscr.move(y, x + i)
            if i >= len(sentence):
                done = True
        stdscr.refresh()

    stdscr.move(y, 80)
    stdscr.addstr(f"  # wrong: {mistakes(keystrokes)}; speed: {cpm(keystrokes)} cpm\n")

    y, x = curses.getsyx()
    stdscr.move(y + 1, 0)
    stdscr.refresh()

    return keystrokes


if __name__ == "__main__":
    wrapper(practice)
