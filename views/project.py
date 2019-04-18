# -*- coding: utf-8 -*-

from controllers.project import ProjectController
from models.project import Project as ModelProject


class Project:

    @staticmethod
    def show_insert_view():
        MP = ModelProject()

        MP.name = raw_input('Nome: ')
        MP.duration = raw_input('Quantidade de horas: ')

        ProjectController().insert(MP)

    @staticmethod
    def show_list_view(option):
        print "\n -> Como deseja realizar a listagem de %s ?" % option
        user_option = input(
            "1 - Listar todos\n"
            "2 - Buscar registro\n"
        )

        if user_option in {1, 2}:
            if user_option == 1:
                ProjectController().list()
            else:
                print 'buscar'
        else:
            raise Exception('Acao %s nao existe' % user_option)