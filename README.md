# Consulta de CEP

Este projeto é uma ferramenta simples para consultar informações de CEPs (Códigos de Endereçamento Postal) utilizando a API ViaCEP. A aplicação permite consultar um único CEP ou uma lista de CEPs, salvando os resultados em arquivos de texto.

## Funcionalidades

- **Consultar CEP Único:** Permite ao usuário inserir um CEP no formato `85887-000` ou `85887000` e obter informações sobre a cidade, estado e região.
- **Consultar CEP com Lista:** Permite ao usuário consultar uma lista de CEPs, onde cada CEP deve estar em um arquivo de texto (`ceps.txt`). Os resultados são salvos em arquivos de texto individuais na pasta `results`.

## Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- `requests`: Biblioteca para realizar requisições HTTP.
- `colorama`: Biblioteca para adicionar cores às saídas no terminal.

Para instalar as dependências, execute o seguinte comando:

```bash
pip install requests colorama
```

## Execute os comandos:

```bash
python script.py

Escolha a opção 1 - Pesquisar CEP.
Escolha a opção 2 - Pesquisar CEP por LISTA.

Os resultados serão salvos na pasta results, onde cada arquivo será nomeado com a cidade correspondente ao CEP.
```


## Estrutura dos arquivos:

```bash
script.py: Script principal para consulta de CEPs.
ceps.txt: Arquivo de texto contendo a lista de CEPs para consulta.
results/: Pasta onde os resultados das consultas serão salvos.
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.

- **GitHub:** [https://github.com/atencioso](https://github.com/atencioso)
