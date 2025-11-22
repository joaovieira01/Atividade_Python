import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        print("Logradouro:", dados.get("logradouro", ""))
        print("Bairro:", dados.get("bairro", ""))
        print("Cidade:", dados.get("localidade", ""))
        print("Estado:", dados.get("uf", ""))

    except Exception:
        print("Falha na requisição. Verifique o CEP ou sua conexão.")

if __name__ == "__main__":
    cep = input("Digite o CEP (somente números): ")
    consultar_cep(cep)
