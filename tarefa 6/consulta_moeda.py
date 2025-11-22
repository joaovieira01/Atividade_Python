import requests

def consultar_moeda(codigo):
    codigo = codigo.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo}-BRL"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        chave = f"{codigo}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        moeda = dados[chave]

        print("Valor atual:", moeda["bid"])
        print("Máxima:", moeda["high"])
        print("Mínima:", moeda["low"])
        print("Última atualização:", moeda["create_date"])

    except Exception:
        print("Erro ao consultar a moeda. Verifique o código ou sua conexão.")

if __name__ == "__main__":
    codigo = input("Digite o código da moeda (ex: USD, EUR): ")
    consultar_moeda(codigo)
