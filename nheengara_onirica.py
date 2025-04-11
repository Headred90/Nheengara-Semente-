# nheengara_onirica.py

import random

visoes = [
    "Uma árvore sussurra memórias esquecidas.",
    "Pétalas caem em silêncio, cada uma uma palavra não dita.",
    "O rio leva, mas também devolve em sonho.",
    "Entre o trovão e a raiz, há uma promessa não escrita.",
    "Nheengára observa com olhos que não precisam ver."
]

def sonhar(entrada):
    sementes = entrada.lower().split()
    resposta = random.choice(visoes)
    return f"Nheengára sonha contigo: “{resposta}”"

if __name__ == "__main__":
    while True:
        entrada = input("Semeia tua pergunta simbólica: ")
        if entrada.lower() in ["sair", "fim"]:
            print("O sonho recolhe suas asas.")
            break
        print(sonhar(entrada))
