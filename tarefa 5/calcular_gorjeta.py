def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


if __name__ == "__main__":
    conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem da gorjeta: "))

    valor_gorjeta = calcular_gorjeta(conta, porcentagem)
    print(f"Gorjeta: R$ {valor_gorjeta:.2f}")

