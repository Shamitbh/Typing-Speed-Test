import curses
from curses import wrapper # used to iniitalize curses module and then restore state after finished

def main(stdscr):
    stdscr.clear() # clears screen from last run
    stdscr.addstr("Hello world") # prints some text to the screen
    stdscr.refresh()
    stdscr.getkey() # makes sure that display on screen stays there and waits for user key entry

wrapper(main)