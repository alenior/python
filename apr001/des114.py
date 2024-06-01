import urllib.request
import urllib.error
import ssl


def verificar_site(url):
    try:
        # Configura o contexto SSL para não verificar certificados
        context = ssl._create_unverified_context()
        # Tenta abrir a URL com o contexto SSL não verificado
        response = urllib.request.urlopen(url, context=context)
        # Se a resposta for um código HTTP 200, o site está disponível
        if response.status == 200:
            return True
    except urllib.error.URLError as e:
        # Captura erros relacionados à URL, como site não encontrado ou indisponível
        print(f"Erro ao acessar o site: {e.reason}")
    except urllib.error.HTTPError as e:
        # Captura erros HTTP, como 404, 500, etc.
        print(f"Erro HTTP: {e.code}")
    except ssl.SSLError as e:
        # Captura erros SSL
        print(f"Erro SSL: {e}")

    return False


# Exemplo de uso
url = "https://www.pudim.com.br"
if verificar_site(url):
    print(f"O site {url} está disponível.")
else:
    print(f"O site {url} não está disponível.")
