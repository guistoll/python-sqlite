# -*- coding: utf-8 -*-

from connections.sqlite import Sqlite
import json


class ProjectController:

    def __init__(self):
        self.conn = Sqlite()
        self.conn.connect()

    def insert(self, project):
        cursor = self.conn.get_cursor()

        cursor.execute("INSERT INTO project (name, duration) VALUES ('%(name)s', %(duration)s)" % project.__dict__)

        self.conn.commit()

    def list(self, search_term=""):
        cursor = self.conn.get_cursor()

        if search_term:
            cursor.execute("SELECT * FROM project p WHERE p.name LIKE '%{}%'".format(search_term))

            self.conn.commit()

            return cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM project ORDER BY project.name")

            self.conn.commit()

            return cursor.fetchall()

    def update(self, id, new_project):
        if new_project.name and new_project.duration:
            cursor = self.conn.get_cursor()

            cursor.execute("UPDATE project SET name = '%s', duration = %s WHERE project.id = %s" % (new_project.name, new_project.duration, id))

            self.conn.commit()

            return True
        else:
            return False

    def delete(self, id):
        cursor = self.conn.get_cursor()

        cursor.execute("DELETE FROM project WHERE project.id = {}".format(id))

        self.conn.commit()

        if cursor.rowcount == 1:
            return True
        else:
            return False

    def check_id_exists(self, id):
        cursor = self.conn.get_cursor()

        cursor.execute("SELECT COUNT(*) FROM project WHERE project.id = {}".format(id))

        self.conn.commit()

        if cursor.fetchone()[0] == 1:
            return True
        else:
            return False

    def export(self):
        project_list = self.list()

        projects_dict = {"project": []}

        for project_dict in project_list:
            project_dict = {
                "id": project_dict["id"],
                "name": project_dict["name"],
                "duration": project_dict["duration"]
            }

            projects_dict["project"].append(project_dict)

        file = open("database.json", "w")

        file.write(json.dumps(projects_dict))

        file.close()
