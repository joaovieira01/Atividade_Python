def calcular_desconto(preco: float, porcentagem: float) -> float:
    return preco * (porcentagem / 100)


def preco_final(preco: float, porcentagem: float) -> float:
    desconto = calcular_desconto(preco, porcentagem)
    return round(preco - desconto, 2)


if __name__ == "__main__":
    preco_original = float(input("Digite o preço do produto: R$ "))
    desconto_percentual = float(input("Digite o percentual de desconto: "))

    final = preco_final(preco_original, desconto_percentual)

    print(f"Preço final após desconto: R$ {final:.2f}")
