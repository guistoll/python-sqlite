# -*- coding: utf-8 -*-

from controllers.project import ProjectController
from models.project import Project as ModelProject


class Project:

    @staticmethod
    def show_insert_view():
        MP = ModelProject()

        MP.name = raw_input("Nome: ")
        MP.duration = raw_input("Quantidade de horas: ")

        ProjectController().insert(MP)

    @staticmethod
    def show_list_view(option):
        print "\n -> Como deseja realizar a listagem de %s ?" % option

        input_user_option = input(
            "1 - Listar todos\n"
            "2 - Buscar registro\n"
        )

        if input_user_option in {1, 2}:
            if input_user_option == 1:
                project_dict = ProjectController().list()

                print project_dict
            else:
                input_user_search = raw_input("-> Informe o nome do registro ou uma parte do nome:\n")

                project_dict = ProjectController().list(input_user_search)

                print project_dict
        else:
            raise Exception('Acao %s nao existe' % input_user_option)

    @staticmethod
    def show_update_view():
        input_user_option = raw_input("\n-> Informe o ID do projeto que deseja ATUALIZAR:\n")

        try:
            int(input_user_option)

            id_exists = ProjectController().check_id_exists(input_user_option)

            if id_exists:
                print "-> Informe os novos dados do projeto:"
                MP = ModelProject()

                MP.name = raw_input("Nome: ")
                MP.duration = raw_input("Quantidade de horas: ")

                update = ProjectController().update(input_user_option, MP)

                if update:
                    print "\nRegistro alterado com sucesso"
                else:
                    print "\nNenhum registro foi alterado!"
            else:
                print "ID {} nao foi encontrado!".format(input_user_option)
        except ValueError:
            print "ID (%s) informado e invalido!" % input_user_option

    @staticmethod
    def show_delete_view():
        input_user_option = raw_input("\n-> Digite o ID do projeto que deseja DELETAR:\n")

        try:
            int(input_user_option)

            delete = ProjectController().delete(input_user_option)

            if delete:
                print "Registro deletado com sucesso!"
            else:
                print "ID {} nao foi encontrado!".format(input_user_option)
        except ValueError:
            print "ID (%s) informado e invalido!" % input_user_option
