from flask import render_template, request, redirect, url_for
from models.questao_model import *


def cadastrar_questao():
    pergunta = request.form.get('pergunta')
    alternativaA = request.form.get('alternativaA')
    alternativaB = request.form.get('alternativaB')
    alternativaC = request.form.get('alternativaC')
    respostaCorreta = request.form.get('respostaCorreta')

    nova_questao = Questao(pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta)
    nova_questao.cadastrarQuestao()
    return redirect(url_for('exibir_lista'))


def exibir_cadastro_questao():
    return render_template('questao/cadastro.html')


def exibir_lista():
    questoes = listaQuestoes
    return render_template('questao/lista.html', questoes=questoes)


def editar_questao():
    id = request.args.get('id')
    questao = Questao.buscar_por_id(id)
    
    if questao is None:
        return redirect(url_for('exibir_lista'))
    
    if request.method == 'GET':
        return render_template('questao/editar_questao.html', pergunta=questao)
    
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        alternativaA = request.form.get('alternativaA')
        alternativaB = request.form.get('alternativaB')
        alternativaC = request.form.get('alternativaC')
        respostaCorreta = request.form.get('respostaCorreta')
        
        questao.editar_questao(pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta)
        return redirect(url_for('exibir_lista'))


def remover_questao():
    id = request.args.get('id')
    questao = Questao.buscar_por_id(id)
    
    if questao is not None:
        questao.remover_questao()
    
    return redirect(url_for('exibir_lista'))
