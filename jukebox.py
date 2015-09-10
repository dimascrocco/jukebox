import curses
from curses.textpad import Textbox, rectangle
from curses import wrapper

def main(stdscr):
	stdscr = curses.initscr()
	stdscr.clear()
	stdscr.addstr(0, 0, "JukeBox - v.0.1 'dancing Saci'")
	editwin = curses.newwin(5,30, 2,1)
	rectangle(stdscr, 1,0,1+5+1, 1+30+1)
	stdscr.refresh()
	
	box = Textbox(editwin)

	box.edit()
	message = box.gather()

wrapper(main)
