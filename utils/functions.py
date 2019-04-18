# -*- coding: utf-8 -*-

from views.project import Project


def insert(option):
    print '\n -> CADASTRO DE', option.upper()

    if option == 'projeto':
        view = Project()
        view.show_insert_view()


def list(option):

    if option == 'projeto':
        view = Project()
        view.show_list_view(option)


def update(option):
    print 'update', option


def delete(option):
    print 'delete', option


def export(option):
    print 'export', option
