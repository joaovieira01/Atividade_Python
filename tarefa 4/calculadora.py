while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: você deve digitar um número válido.\n")
        continue

    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            if n2 == 0:
                raise ZeroDivisionError
            resultado = n1 / n2
        else:
            raise ValueError("Operação inválida")

    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.\n")
        continue
    except ValueError:
        print("Erro: operação inválida. Use +, -, *, /.\n")
        continue

    print(f"Resultado: {resultado}")
    break
