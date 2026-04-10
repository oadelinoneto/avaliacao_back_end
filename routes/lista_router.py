from flask import Flask
from controllers import lista_controller

def adicionar_rotas_lista(app: Flask):
    app.add_url_rule('/lista', endpoint='exibir_lista', view_func=lista_controller.exibir_lista, methods=['GET'])
    app.add_url_rule(rule='/editar_questao', view_func=lista_controller.editar_questao, endpoint='editar_questao', methods=['GET', 'POST'])
    app.add_url_rule(rule='/remover_questao', view_func=lista_controller.remover_questao, endpoint='remover_questao', methods=['GET'])