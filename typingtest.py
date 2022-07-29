import curses
from curses import wrapper # used to iniitalize curses module and then restore state after finished

def startingScreen(stdscr):
    # clears screen from last run
    stdscr.clear()
    # prints welcome message to screen
    stdscr.addstr("Welcome to the Typing Speed Test!")
    stdscr.addstr("\nPress any key to begin: ") 
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)

def main(stdscr):
     # create curses color pairs foreground/background with different int ID's
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    startingScreen(stdscr)
    
wrapper(main)