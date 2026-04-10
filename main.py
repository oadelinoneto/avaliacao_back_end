from flask import Flask
from routes import index_router, cadastro_router, lista_router

app = Flask(__name__)
index_router.adicionar_index(app)
cadastro_router.adicionar_rotas_cadastro(app)
lista_router.adicionar_rotas_lista(app)