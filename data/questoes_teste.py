from models.questao_model import Questao


def carregar_questoes_teste():
    questoes = [
        ("Qual é a capital da França?", "Paris", "Londres", "Berlim", "A"),
        ("Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "B"),
        ("Quanto é 2 + 2?", "3", "4", "5", "B"),
        ("Qual é o maior planeta do Sistema Solar?", "Terra", "Marte", "Júpiter", "C"),
        ("Qual linguagem é usada neste projeto web?", "Python", "Java", "C#", "A"),
        ("Qual é o resultado de 10 - 4?", "6", "5", "4", "A"),
        ("Qual é a cor do céu em um dia sem nuvens?", "Azul", "Vermelho", "Verde", "A"),
        ("Qual animal é conhecido por mia?", "Cachorro", "Gato", "Pássaro", "B"),
        ("Quantos dias tem uma semana?", "5", "6", "7", "C"),
        ("Qual é o oposto de 'dia'?", "Noite", "Sol", "Chuva", "A"),
        ("Qual destes é um número par?", "7", "9", "8", "C"),
        ("Qual fruta é tradicionalmente vermelha por fora e tem sementes pequenas?", "Maçã", "Banana", "Uva", "A"),
        ("Qual é a soma de 1 + 1?", "1", "2", "3", "B"),
        ("Qual planeta é o nosso lar?", "Mercúrio", "Terra", "Vênus", "B"),
        ("Qual é o líquido que bebemos para nos hidratar?", "Água", "Óleo", "Areia", "A"),
        ("Qual é o primeiro mês do ano?", "Janeiro", "Fevereiro", "Março", "A"),
        ("Qual instrumento mede a temperatura?", "Régua", "Termômetro", "Balança", "B"),
        ("Qual é o resultado de 3 x 3?", "6", "9", "12", "B"),
        ("Qual é o continente onde fica o Brasil?", "Europa", "África", "América do Sul", "C"),
        ("Qual destes é um animal marinho?", "Leão", "Golfinho", "Cavalo", "B"),
    ]

    for pergunta, alternativa_a, alternativa_b, alternativa_c, resposta_correta in questoes:
        questao = Questao(pergunta, alternativa_a, alternativa_b, alternativa_c, resposta_correta)
        questao.cadastrarQuestao()
