from flask import Flask
from controllers import questao_controller


def adicionar_rotas_questao(app: Flask):
    app.add_url_rule('/questao/cadastro', endpoint='cadastro', view_func=questao_controller.exibir_cadastro_questao, methods=['GET'])
    app.add_url_rule('/questao/cadastro', endpoint='cadastrar_questao', view_func=questao_controller.cadastrar_questao, methods=['POST'])
    app.add_url_rule('/questao/lista', endpoint='exibir_lista', view_func=questao_controller.exibir_lista, methods=['GET'])
    app.add_url_rule('/questao/editar_questao', endpoint='editar_questao', view_func=questao_controller.editar_questao, methods=['GET', 'POST'])
    app.add_url_rule('/questao/remover_questao', endpoint='remover_questao', view_func=questao_controller.remover_questao, methods=['GET'])
