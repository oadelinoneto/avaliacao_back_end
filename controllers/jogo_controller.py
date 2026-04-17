from flask import Flask, render_template, request, redirect, url_for
from models.questao_model import *
import random




def pagina_inicial_jogo():
    return render_template('jogo/pagina_inicial.html')


def sem_questoes():
    return render_template('jogo/sem_questoes.html')


def continuar_jogo():
    if not listaQuestoes:
        return redirect(url_for('sem_questoes'))
    
    questao = random.choice(listaQuestoes)
    return render_template('jogo/pagina_jogo.html', jogo=inicializar_jogo, questao=questao)


def inicio_jogo():
    global inicializar_jogo
    
    inicializar_jogo = {
    'perguntas': 0,
    'acertos': 0,
    'erros': 0
    }

    questoes = listaQuestoes
    
    if questoes:
        questao = random.choice(questoes)
        return render_template('jogo/pagina_jogo.html', jogo=inicializar_jogo, questao=questao)

    return redirect(url_for('sem_questoes'))

def responder_questao():
    id_questao = request.form.get('id_questao')
    resposta_jogador = request.form.get('resposta')
    questao = Questao.buscar_por_id(id_questao)

    if not listaQuestoes or questao is None:
        return redirect(url_for('sem_questoes'))

    inicializar_jogo['perguntas'] += 1
    
    acertou = questao.resposta_correta(resposta_jogador)

    if acertou:
        inicializar_jogo['acertos'] += 1
    else:
        inicializar_jogo['erros'] += 1

    return render_template(
        'jogo/resultado.html',
        jogo=inicializar_jogo,
        questao=questao,
        resposta_jogador=resposta_jogador,
        acertou=acertou,
    )