import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("Nome:", nome)
        print("E-mail:", email)
        print("País:", pais)

    except Exception:
        print("Falha ao buscar usuário. Verifique sua conexão ou tente novamente.")

if __name__ == "__main__":
    buscar_usuario()
