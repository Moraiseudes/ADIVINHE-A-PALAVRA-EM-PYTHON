import random

palavras = ["roteador", "firewall", "protocolo", "endereço", "gateway", "domínio", "servidor", "firewall", "navegador", "download"]

def escolher_palavra():
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:random
    if letra in letras_corretas:
            palavra_oculta += letra
        
            palavra_oculta += "_"
    return palavra_oculta

def jogo():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 8

    print("Bem-vindo ao Adivinhe a Palavra - Fundamentos de Redes e Computadores!")
    print("Adivinhe a palavra relacionada a redes e computadores.")
    print(mostrar_palavra_oculta(palavra, letras_corretas))

    while tentativas > 0:
        tentativa = input("\nDigite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if tentativa in letras_corretas:
            print("Você já tentou essa letra.")
            continue

        if tentativa in palavra:
            letras_corretas.append(tentativa)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

        palavra_oculta = mostrar_palavra_oculta(palavra, letras_corretas)
        print(palavra_oculta)

        if palavra_oculta == palavra:
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == 0:
        print("Você perdeu! A palavra era:", palavra)

jogo()