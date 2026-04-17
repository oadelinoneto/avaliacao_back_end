from flask import Flask
from controllers import jogo_controller

def adicionar_jogo(app : Flask):
    app.add_url_rule(rule='/inicio', endpoint='pagina_inicial_jogo', view_func=jogo_controller.pagina_inicial_jogo, methods=['GET'])
    app.add_url_rule(rule='/jogo', endpoint='inicio_jogo', view_func=jogo_controller.inicio_jogo, methods=['GET'])
    app.add_url_rule(rule='/jogo/continuar', endpoint='continuar_jogo', view_func=jogo_controller.continuar_jogo, methods=['POST'])
    app.add_url_rule(rule='/jogo/sem_questoes', endpoint='sem_questoes', view_func=jogo_controller.sem_questoes, methods=['GET'])
    app.add_url_rule(rule='/jogo/responder', endpoint='responder_questao', view_func=jogo_controller.responder_questao, methods=['POST'])