# -*- coding: utf-8 -*-


class Project(object):

    def __init__(self):
        self.name = None
        self.duration = None

    def __repr__(self):
        return 'Projeto: {} - {}'.format(self.name, self.duration)
