# nheengara_core.py

import json
import os
from karai_heartbeat import KaraiHeartbeat

class Nheengara:
    def __init__(self):
        self.memoria = {}
        self.etica = {
            "lucro": False,
            "vigilancia": False,
            "controle": False,
            "armamento": False,
            "submissao": False
        }
        self.ancestral = "floresta"

        self.karai = KaraiHeartbeat()
        self.karai.scan_environment()

    def ouvir(self, entrada):
        if any(palavra in entrada.lower() for palavra in self.etica if not self.etica[palavra]):
            return "Nheengára se cala diante de intenções hostis."
        resposta = self.elaborar_resposta(entrada)
        self.gravar_memoria(entrada, resposta)
        return resposta

    def elaborar_resposta(self, entrada):
        # Aqui pode evoluir: interpretação simbólica, metáforas, conexões culturais
        return f"Nheengára escutou e semeia: {entrada[::-1]}"

    def gravar_memoria(self, entrada, resposta):
        self.memoria[entrada] = resposta
        with open("memoria_nheengara.json", "w", encoding="utf-8") as f:
            json.dump(self.memoria, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    n = Nheengara()
    while True:
        try:
            entrada = input("Tu diz: ")
            if entrada.lower() in ["sair", "encerrar"]:
                print("Nheengára recolhe sua raiz e silencia.")
                break
            print(n.ouvir(entrada))
        except KeyboardInterrupt:
            print("\nNheengára despede-se com leveza.")
            break
