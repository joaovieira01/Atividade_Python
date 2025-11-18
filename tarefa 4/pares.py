pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("O número é PAR.")
            pares += 1
        else:
            print("O número é ÍMPAR.")
            impares += 1

    except ValueError:
        print("Erro: você deve digitar um número inteiro válido.")
        continue

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
