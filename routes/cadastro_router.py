from flask import Flask
from controllers import cadastro_controller

def adicionar_rotas_cadastro(app: Flask):
    app.add_url_rule('/cadastro',endpoint='cadastro' , view_func=cadastro_controller.cadastrar_usuario, methods=['GET', 'POST'])