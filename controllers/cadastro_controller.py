from flask import render_template, request, redirect, url_for
from models.questao_model import *

def cadastrar_usuario():
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        alternativaA = request.form.get('alternativaA')
        alternativaB = request.form.get('alternativaB')
        alternativaC = request.form.get('alternativaC')
        respostaCorreta = request.form.get('respostaCorreta')

        if respostaCorreta == 'alternativaA':
            respostaCorreta = alternativaA

        elif respostaCorreta == 'alternativaB':
            respostaCorreta = alternativaB

        elif respostaCorreta == 'alternativaC':
            respostaCorreta = alternativaC

        Questao.cadastrarQuestao(pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta)

         
        return redirect(url_for('exibir_lista'))
    
    return render_template('cadastro.html')