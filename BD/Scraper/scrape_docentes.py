# bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da pagina-alvo do scraper
url = 'https://www.ifpb.edu.br/ppgti/programa/corpo-docente'

# requisição HTTP
response = requests.get(url)
if response.status_code == 200:
    # Parsing do HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # procura os dados dos docentes permanentes
    docentes_permanentes = soup.find('div', id='parent-fieldname-text').find_all('h4')
    
    # os dados dos docentes serão armazenados aqui
    data = []
    
    # Itera sobre os docentes permanentes
    for docente in docentes_permanentes:
        nome = docente.text.strip()
        linha_pesquisa = docente.find_next('p').text.stripx().split(':')[1].strip()
        url_lattes = docente.find_next('a')['href']
        
        # Encontra a próxima tag <p> após o nome do docente
        tag_p_email = docente.find_next_sibling('p')
        
        # Extrai o e-mail se a tag for encontrada e contiver "E-mail:"
        if tag_p_email and 'E-mail:' in tag_p_email.text:
            email = tag_p_email.text.strip().split('E-mail:')[1].strip()
        else:
            email = None
        
        # Adiciona os dados do docente à lista
        data.append({'Nome': nome, 'Linha de Pesquisa': linha_pesquisa, 'URL do Lattes': url_lattes, 'E-mail': email})
    
    # Cria o DataFrame
    df = pd.DataFrame(data)
    
    # Exibe o DataFrame
    print(df)
else:
    print('Falha ao acessar a página:', response.status_code)