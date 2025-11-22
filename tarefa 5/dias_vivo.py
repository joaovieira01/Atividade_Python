from datetime import datetime

def calcular_dias_vivo(data_nascimento: str) -> int:
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    diferenca = hoje - nascimento
    return diferenca.days


if __name__ == "__main__":
    data = input("Digite sua data de nascimento (DD/MM/AAAA): ")

    dias = calcular_dias_vivo(data)
    print(f"Você está vivo há {dias} dias.")
