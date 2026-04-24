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
        self.erros = []

    def cadastrarQuestao(self):
        listaQuestoes.append(self)
        return self
    
    def editar_questao(self, pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta):
        self.pergunta = pergunta
        self.alternativaA = alternativaA
        self.alternativaB = alternativaB
        self.alternativaC = alternativaC
        self.respostaCorreta = respostaCorreta
        return self
    
    def validar_questao(self):

        if not self.pergunta:
            self.erros.append("Campo pergunta obrigatório.")

        if not self.alternativaA:
            self.erros.append("Campo alternativa A obrigatório.")

        if not self.alternativaB:
            self.erros.append("Campo alternativa B obrigatório.")

        if not self.alternativaC:
            self.erros.append("Campo alternativa C obrigatório.")

        return self.erros     
        

    def remover_questao(self):
        listaQuestoes.remove(self)
        return True
    
    def resposta_correta(self, resposta):
        if resposta == self.respostaCorreta:
            return True

        return False
    
    @classmethod
    def buscar_por_id(cls, id):
        for questao in listaQuestoes:
            if str(questao.id) == str(id):
                return questao
        return None