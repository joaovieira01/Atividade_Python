def classificador_idade():
    idade = int(input("Digite sua idade: "))

    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    elif idade >= 60:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida"

    print(f"Classificação: {categoria}")


if __name__ == "__main__":
    classificador_idade()

