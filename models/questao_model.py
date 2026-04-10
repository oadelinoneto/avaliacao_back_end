listaQuestoes = []
id = 1

class Questao:
    def __init__(self, pergunta:str, alternativaA:str, alternativaB:str, alternativaC:str, respostaCorreta:str):
        global id
        self.id = id
        id += 1
        self.pergunta = pergunta
        self.alternativaA = alternativaA
        self.alternativaB = alternativaB
        self.alternativaC = alternativaC
        self.respostaCorreta = respostaCorreta

    @classmethod
    def cadastrarQuestao(cls, pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta):
        novaQuestao = cls(pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta)
        listaQuestoes.append(novaQuestao)
        return novaQuestao
    
    @classmethod
    def exibirQuestoes(cls):
        return listaQuestoes

Questao.cadastrarQuestao('questao 1', 'oi', 'oi', 'oi', 'oi')

Questao.cadastrarQuestao('questao 2', 'ola', 'ola', 'ola', 'ola')