from flask import Flask
from controllers import index_controller

def adicionar_index(app : Flask):
    app.add_url_rule(rule='/', endpoint='index', view_func=index_controller.index, methods=['GET'])