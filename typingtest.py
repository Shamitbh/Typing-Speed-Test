import curses
from curses import wrapper # used to iniitalize curses module and then restore state after finished

def starting_screen(stdscr):
    # clears screen from last run
    stdscr.clear()
    # prints welcome message to screen
    stdscr.addstr("Welcome to the Typing Speed Test!")
    stdscr.addstr("\nPress any key to begin: ") 
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, targetText, currentText, wpm=0):
    stdscr.addstr(targetText, curses.color_pair(3))
    # loop through current text and display overlaying the target text
    for i, char in enumerate(currentText):
        # check if the current text is the correct char. If so display in green, otherwise red.
        correctChar = targetText[i]
        color = curses.color_pair(1) # change text color to green
        if char != correctChar:
            color = curses.color_pair(2)  # change text color to red
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    targetText = "Hello World! This is some sample text for the wpm test!"
    currentText = []
    
    while True:
        stdscr.clear()
        display_text(stdscr, targetText, currentText)
        stdscr.refresh()

        # get key from user
        key = stdscr.getkey()

        # check if key is escape and if so exit loop
        if ord(key) == 27: 
            break
        # check if key is backspace and append to current text accordingly
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(currentText) > 0:
                currentText.pop()
        elif len(currentText) < len(targetText):
            currentText.append(key)

def main(stdscr):
     # create curses color pairs foreground/background with different int ID's
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    starting_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)