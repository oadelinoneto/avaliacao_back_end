from flask import render_template, request, redirect, url_for
from models.questao_model import *

def exibir_lista():
    questoes = listaQuestoes
    return render_template('lista.html', questoes=questoes)

def editar_questao():
    id = request.args.get('id')

    for questao in listaQuestoes:
        if str(questao.id) == id:
            return render_template('editar_questao.html', pergunta=questao)
        
    if request.method == 'POST':
        id = request.form.get('id')
        pergunta = request.form.get('pergunta')
        alternativaA = request.form.get('alternativaA')
        alternativaB = request.form.get('alternativaB')
        alternativaC = request.form.get('alternativaC')
        respostaCorreta = request.form.get('respostaCorreta')

        for questao in listaQuestoes:
            if str(questao.id) == id:
                questao.pergunta = pergunta
                questao.alternativaA = alternativaA
                questao.alternativaB = alternativaB
                questao.alternativaC = alternativaC
                questao.respostaCorreta = respostaCorreta

                return redirect(url_for('exibir_lista'))
            

def remover_questao():
    id = request.args.get('id')

    for questao in listaQuestoes:
        if str(questao.id) == id:
            listaQuestoes.remove(questao)
            return redirect(url_for('exibir_lista'))