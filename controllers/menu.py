# -*- coding: utf-8 -*-

from utils import functions


class MenuController:

    # retorna texto do valor que usuario informou
    # Ex: usuario informa `2` - retorna `funcionario`
    @staticmethod
    def options(user_input_option):
        options_dict = {
            '1': 'projeto',
            '2': 'funcionario',
            '3': 'atividade',
            '4': 'empresa',
        }

        if user_input_option in options_dict:
            return options_dict[user_input_option]
        else:
            raise Exception('Opcao %s nao existe' % user_input_option)

    # usuario seleciona acao do registro
    @staticmethod
    def actions(user_option, user_input_action):
        actions_dict = {
            '1': functions.insert,
            '2': functions.list,
            '3': functions.update,
            '4': functions.delete,
            '5': functions.export,
        }

        # pega nome da funcao dentro de `actions_map` de acordo
        # com `user_input_action` e chama, passando parametro `user_option`
        # ou retorna excecao
        if user_input_action in actions_dict:
            actions_dict[user_input_action](user_option)
        else:
            raise Exception('Acao %s nao existe' % user_input_action)
