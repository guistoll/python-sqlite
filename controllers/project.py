# -*- coding: utf-8 -*-

from connections.sqlite import Sqlite


class ProjectController:

    def __init__(self):
        self.conn = Sqlite()
        self.conn.connect()

    def insert(self, project):
        cursor = self.conn.get_cursor()

        cursor.execute("INSERT INTO project (name, duration) VALUES ('%(name)s', %(duration)s)" % project.__dict__)

        self.conn.commit()

    def list(self, search_term):
        cursor = self.conn.get_cursor()

        cursor.execute("SELECT * FROM project")

        projects_dict

