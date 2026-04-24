from flask import Flask, render_template, request, redirect, url_for
from models.questao_model import *
import random




def pagina_inicial_jogo():
    return render_template('jogo/pagina_inicial.html')


def sem_questoes():
    return render_template('jogo/sem_questoes.html')


def fim_jogo():
    if 'inicializar_jogo' not in globals():
        return redirect(url_for('pagina_inicial_jogo'))

    return render_template('jogo/fim_jogo.html', jogo=inicializar_jogo)


def continuar_jogo():
    if not listaQuestoes:
        return redirect(url_for('sem_questoes'))

    questoes_restantes = inicializar_jogo.get('questoes_restantes', [])

    if not questoes_restantes:
        return redirect(url_for('fim_jogo'))

    id_questao = random.choice(questoes_restantes)
    questao = Questao.buscar_por_id(id_questao)

    if questao is None:
        questoes_restantes.remove(id_questao)

        if not questoes_restantes:
            return redirect(url_for('fim_jogo'))

        return continuar_jogo()

    return render_template('jogo/pagina_jogo.html', jogo=inicializar_jogo, questao=questao)


def inicio_jogo():
    global inicializar_jogo
    
    inicializar_jogo = {
        'perguntas': 0,
        'acertos': 0,
        'erros': 0,
        'questoes_restantes': []
    }

    questoes = listaQuestoes
    
    if questoes:
        for questao in questoes:
            inicializar_jogo['questoes_restantes'].append(questao.id)

        id_questao = random.choice(inicializar_jogo['questoes_restantes'])
        questao = Questao.buscar_por_id(id_questao)

        if questao is None:
            return redirect(url_for('sem_questoes'))

        return render_template('jogo/pagina_jogo.html', jogo=inicializar_jogo, questao=questao)

    return redirect(url_for('sem_questoes'))

def responder_questao():
    id_questao = request.form.get('id_questao')
    resposta_jogador = request.form.get('resposta')
    questao = Questao.buscar_por_id(id_questao)

    if not listaQuestoes or questao is None:
        return redirect(url_for('sem_questoes'))

    questoes_restantes = inicializar_jogo.get('questoes_restantes', [])

    if questao.id in questoes_restantes:
        questoes_restantes.remove(questao.id)

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