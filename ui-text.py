import curses
import main as mainCaller
import webbrowser

menu = ['Start Pinging 🏓🔔', 'Advanced (Coming soon...⌛)', 'Visit Developer 💻', 'Exit ❌']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
    		# if user selected last row, exit the program
            if current_row == len(menu)-1:
                break
    		# if user selected last row, exit the program
            if current_row == len(menu)-4:
                print("Your connection is being tested, we'll notify with your connection state!")
                mainCaller.pingServer()
                
            if current_row == len(menu)-2:
                webbrowser.open_new('ItsMsalati.ly')

        print_menu(stdscr, current_row)


curses.wrapper(main)