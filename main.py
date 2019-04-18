# -*- coding: utf-8 -*-

from views.menu import Menu
from connections.sqlite import Sqlite

if __name__ == "__main__":

    conn = Sqlite()
    conn.connect()

    view = Menu(conn)
    view.show_menu_options()
