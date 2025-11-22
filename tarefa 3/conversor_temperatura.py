def conversor_temperatura():
    temp = float(input("Digite a temperatura: "))
    origem = input("Unidade de origem (C/F/K): ").upper()
    destino = input("Unidade de destino (C/F/K): ").upper()

    # Converte origem para Celsius
    if origem == "C":
        celsius = temp
    elif origem == "F":
        celsius = (temp - 32) * 5 / 9
    elif origem == "K":
        celsius = temp - 273.15
    else:
        print("Unidade de origem inválida.")
        return

    # Converte Celsius para destino
    if destino == "C":
        resultado = celsius
    elif destino == "F":
        resultado = (celsius * 9 / 5) + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:
        print("Unidade de destino inválida.")
        return

    print(f"Temperatura convertida: {resultado:.2f} {destino}")


if __name__ == "__main__":
    conversor_temperatura()

