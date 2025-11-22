import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        if tamanho <= 0:
            print("O tamanho deve ser maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print("Senha gerada:", senha)
    except ValueError:
        print("Digite apenas números válidos.")
