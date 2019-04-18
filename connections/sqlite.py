# -*- coding: utf-8 -*-

import os
import sqlite3


class Sqlite(object):

    def __init__(self):
        self.conn = None
        self.dbname = "database.db"
        self.dbexists = os.path.exists(self.dbname)

    def connect(self):
        self.conn = sqlite3.connect(self.dbname)
        self.manage_database()

    def commit(self):
        self.conn.commit()

    def get_cursor(self):
        return self.conn.cursor()

    def manage_database(self):
        """" Criar estrutura das tabelas quando o database.db não existia localmente """
        if self.dbexists:
            return

        cursor = self.get_cursor()
        self.dbexists = True

        # CREATE TABLE PROJECT (name, duration)
        cursor.execute("CREATE TABLE IF NOT EXISTS project (\
                       id INTEGER PRIMARY KEY,\
                       name VARCHAR(50),\
                       duration INTEGER)")

        # CREATE TABLE ATIVIDADE
        # cursor.execute("")
