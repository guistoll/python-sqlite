# -*- coding: utf-8 -*-

from controllers.menu import MenuController


class Menu:

    def __init__(self, connection=None):
        self.menu = MenuController()
        self.connection = connection

    def show_menu_options(self):
        user_input_option = raw_input(
            '-> Selecione uma opcao: \n\
            1 - Projeto \n\
            2 - Funcionario \n\
            3 - Atividade \n\
            4 - Empresa \n'
        )

        user_option = self.menu.options(user_input_option)

        self.show_menu_actions(user_option)

    def show_menu_actions(self, user_option):
        user_input_action = raw_input(
            '\n-> Selecione uma acao para {}: \n\
            1 - Cadastrar \n\
            2 - Listar \n\
            3 - Editar \n\
            4 - Deletar \n\
            5 - Exportar \n'
            .format(user_option.upper())
        )

        self.menu.actions(user_option, user_input_action)
