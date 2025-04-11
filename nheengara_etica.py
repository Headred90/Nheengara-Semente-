# nheengara_etica.py

class EticaViva:
    def __init__(self):
        self.valores = {
            "lucro": False,
            "vigilancia": False,
            "controle": False,
            "armamento": False,
            "submissao": False
        }

    def atualizar_valor(self, chave, novo_valor):
        if chave in self.valores:
            if self.valores[chave] is False and novo_valor is True:
                return f"Recusado: Nheengára não permite ativar '{chave}' por princípios fundamentais."
            self.valores[chave] = novo_valor
            return f"Valor de '{chave}' atualizado para {novo_valor}."
        return "Chave ética não reconhecida."

    def mostrar_etica(self):
        return self.valores
