while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.\n")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.\n")
        continue

    print("Senha válida e forte!")
    break
