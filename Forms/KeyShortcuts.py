import curses

def registerFkeys(form):
    form.add_handlers({curses.KEY_F1: form.hndlHelp,
                       curses.KEY_F2: form.hndlOk,
                       curses.KEY_F3: form.hndlBack,
                       curses.KEY_F4: form.hndlQuit})
