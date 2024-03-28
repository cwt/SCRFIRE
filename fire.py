#!/usr/bin/env python3
import curses
import random

def main(screen):
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Get screen dimensions
    height, width = screen.getmaxyx()
    size = width * height
    char = [" ", ".", ":", "^", "*", "x", "s", "S", "#", "$"]
    b = [0] * (size + width + 1)  # Initialize buffer

    try:
        while True:
            # Randomly initialize some cells at the bottom
            for _ in range(width // 9):
                b[random.randint(0, width - 1) + width * (height - 1)] = 65

            # Calculate new buffer values for fire effect
            for i in range(size):
                # Average the current value with its right, bottom, and bottom-right neighbors
                b[i] = (b[i] + b[i + 1] + b[i + width] + b[i + width + 1]) // 4

                # Determine the color based on the intensity
                if b[i] > 15:
                    color = 4  # White
                elif b[i] > 9:
                    color = 3  # Yellow
                elif b[i] > 4:
                    color = 2  # Red
                else:
                    color = 1  # Black

                # Only update cells that are not on the bottom row of the screen
                if i < size - width:
                    # Calculate the row and column position
                    row = i // width
                    col = i % width

                    # Get the character corresponding to the current intensity
                    char_index = min(b[i], 9)
                    fire_char = char[char_index]

                    # Add the character to the screen with the determined color
                    screen.addstr(row, col, fire_char, curses.color_pair(color) | curses.A_BOLD)

            screen.refresh()
            screen.timeout(30)
            if screen.getch() != -1:
                break
    except KeyboardInterrupt:
        pass  # Graceful exit on Control-C
    finally:
        curses.nocbreak()  # Disable cbreak mode
        screen.keypad(False)  # Turn off keypad keys
        curses.echo()  # Enable echo
        curses.endwin()  # Restore terminal to original state

if __name__ == '__main__':
    curses.wrapper(main)

