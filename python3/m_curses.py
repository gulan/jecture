#!/usr/bin/env python3

import curses

"""
baudrate
beep
can_change_color
cbreak
color_content
color_pair
curs_set
def_prog_mode
def_shell_mode
delay_output
doupdate
echo
endwin
erasechar
error
filter
flash
flushinp
getmouse
getsyx
getwin
halfdelay
has_colors
has_ic
has_il
has_key
init_color
init_pair
initscr
intrflush
is_term_resized
isendwin
keyname
killchar
longname
meta
mouseinterval
mousemask
napms
newpad
newwin
nl
nocbreak
noecho
nonl
noqiflush
noraw
pair_content
pair_number
putp
qiflush
raw
reset_prog_mode
reset_shell_mode
resetty
resize_term
resizeterm
savetty
setsyx
setupterm
start_color
termattrs
termname
tigetflag
tigetnum
tigetstr
tparm
typeahead
unctrl
unget_wch
ungetch
ungetmouse
update_lines_cols
use_default_colors
use_env
version
wrapper
"""

def curses_02():
    def main(stdscr):
        stdscr.addstr(0, 0, 'Hello, World!')
        stdscr.addstr(1, 4, 'Lines={}'.format(curses.LINES))
        stdscr.addstr(2, 4, 'Cols={}'.format(curses.COLS))
        stdscr.refresh()
        stdscr.getkey()
    curses.wrapper(main)

if __name__ == '__main__':
    curses_02()

