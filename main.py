from flask import Flask
from routes import index_router, questao_router, jogo_router
from data.questoes_teste import carregar_questoes_teste

app = Flask(__name__)
index_router.adicionar_index(app)
questao_router.adicionar_rotas_questao(app)
jogo_router.adicionar_jogo(app)
carregar_questoes_teste()