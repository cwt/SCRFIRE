#!/usr/bin/env python3
import curses
import random

def main(screen):
    curses.curs_set(0)  # Hide cursor
    curses.start_color()  # Start color mode
    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Get screen dimensions
    height, width = screen.getmaxyx()
    size = width * height
    char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b = [0] * (size + width + 1)  # Initialize buffer

    while True:
        # Randomly initialize some cells at the bottom
        for _ in range(width // 9):
            b[random.randint(0, width - 1) + width * (height - 1)] = 65

        # Calculate new buffer values
        for i in range(size):
            b[i] = (b[i] + b[i + 1] + b[i + width] + b[i + width + 1]) // 4
            color = 4 if b[i] > 15 else (3 if b[i] > 9 else (2 if b[i] > 4 else 1))

            if i < size - width:
                screen.addstr(i // width, i % width, char[min(b[i], 9)], 
                              curses.color_pair(color) | curses.A_BOLD)

        screen.refresh()
        screen.timeout(30)
        if screen.getch() != -1:
            break

    curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)

