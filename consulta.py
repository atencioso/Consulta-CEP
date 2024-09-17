import os
import requests
import re
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def formatar_cep(cep):
    """ Formata o CEP no formato 85887-000 """
    return re.sub(r'(\d{5})(\d{3})', r'\1-\2', cep)

def consultar_cep(cep):
    """ Consulta o CEP na API ViaCEP e retorna os dados """
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if 'erro' in dados:
            print(Fore.RED + f"CEP {cep} não encontrado.")
            return None
        return dados
    else:
        print(Fore.RED + "Erro ao consultar o CEP.")
        return None

def criar_pasta_results():
    """ Cria a pasta results se ela não existir """
    if not os.path.exists('results'):
        os.makedirs('results')

def salvar_resultado(nome_arquivo, dados):
    """ Salva os dados em um arquivo TXT """
    with open(nome_arquivo, 'w') as f:
        f.write(f"Cidade: {dados['localidade']}\n")
        f.write(f"Estado: {dados['uf']}\n")
        f.write(f"Região: {dados['regiao']}\n")

def consultar_ceps_lista(arquivo_lista):
    """ Consulta uma lista de CEPs e salva os resultados em arquivos TXT """
    criar_pasta_results()  # Garante que a pasta results exista
    
    with open(arquivo_lista, 'r') as arquivo:
        ceps = arquivo.readlines()
    
    for cep in ceps:
        cep = cep.strip()
        if not re.match(r'^\d{5}-\d{3}$', cep):
            cep = formatar_cep(cep)  # Formata o CEP se não estiver no formato correto
        dados = consultar_cep(cep)
        if dados:
            nome_arquivo = f"results/{dados['localidade']}.txt"
            salvar_resultado(nome_arquivo, dados)

def consultar_cep_unico():
    """ Consulta um único CEP """
    cep = input(Fore.WHITE + "Digite o CEP (formato 85887-000 ou 85887000): ").strip()
    if not re.match(r'^\d{5}-\d{3}$', cep):
        cep = formatar_cep(cep)  # Formata o CEP se não estiver no formato correto
    
    dados = consultar_cep(cep)
    if dados:
        print(Fore.GREEN + f"Cidade: {dados['localidade']}")
        print(Fore.GREEN + f"Estado: {dados['uf']}")
        print(Fore.GREEN + f"Região: {dados['regiao']}")

def menu():
    """ Exibe o menu e processa a escolha do usuário """
    print(Fore.GREEN + "Escolha uma opção:")
    print(Fore.GREEN + "1 - Pesquisar CEP único")
    print(Fore.GREEN + "2 - Pesquisar CEP com LISTA")
    escolha = input(Fore.WHITE + "Digite o número da opção desejada: ").strip()
    
    if escolha == '1':
        consultar_cep_unico()
    elif escolha == '2':
        arquivo_lista = 'ceps.txt'
        consultar_ceps_lista(arquivo_lista)
    else:
        print(Fore.RED + "Opção inválida.")

if __name__ == "__main__":
    menu()
