# -*- coding: utf-8 -*-

from views.project import Project
from controllers.project import ProjectController


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

    if option == 'projeto':
        view = Project()
        view.show_update_view()


def delete(option):

    if option == 'projeto':
        view = Project()
        view.show_delete_view()


def export(option):

    if option == 'projeto':
        ctrl = ProjectController()
        ctrl.export()
