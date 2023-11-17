

# Vinylhunter API
![](https://github.com/GeorgeDomingos/semsufoco-controle-financeiro-API-REST/assets/136137653/33045d14-8ce0-44d8-b5c2-abf92dd03129)



<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/GeorgeDomingos/vinyl-hunter-API?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/GeorgeDomingos/vinyl-hunter-API">
  
  <a href="https://github.com/GeorgeDomingos/semsufoco-controle-financeiro-API-REST/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/GeorgeDomingos/vinyl-hunter-API">
  </a>

  
   <a href="https://github.com/GeorgeDomingos">
    <img alt="Feito por George Domingos" src="https://img.shields.io/badge/feito-por%20George%20Domingos-D818A5?style=social">
   </a>
   
   <a href="https://github.com/GeorgeDomingos/semsufoco-controle-financeiro-API-REST/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/GeorgeDomingos/vinyl-hunter-API?style=social">
  </a>

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Como Executar](#-como-executar-o-projeto) •
[Tecnologias](#-tecnologias) •
[Endpoints da API](#-endpoints-da-api) •
[Implementações Futuras](#-implementações-futuras) •
[Referências](#-referências) •
[Contribuidores](#-contribuidores)
  
## 📂 Sobre o projeto

A Vinyhunter API foi desenvolvida como trabalho final do módulo de Introdução à Engenharia de Dados do Programa FAST - Formação Acelerada em Análise e visualização de Dados - CESAR School. O projeto foi criado para aplicar os conceitos de ETL (Extract, Transform e Load) e Web Scraping.

O projeto usa a API do Discogs como fonte de dados para extrair informações sobre os discos que possuam versões na mídia vinil existentes com base no artista consultado. Em uma segunda etapa, é feito o tratamento da consulta obtida e a formatação com as informações mais relevantes (id, título, gravadora, ano e formato e o país onde o disco foi produzido). Na última etapa, o resultado pode ser exibido em um formato JSON ou armazenado em banco de dados NoSQL MongoDB.

A Vinylhunter também permite ao usuário obter uma minibiografia do artista consultado. A API realiza uma consulta ao site da Wikipedia e com o uso da bilioteca Beatifulsoup é feito uma Web Scraping da tabela com as informações básicas do artista, o resultado é tratado e depois pode ser exibido em formato JSON ou armazenado em banco de dados NoSQL MongoDB.


## 💻 Funcionalidades
- Discos de vinil:
  - [x] Obter uma lista com todos os discos no formato vinil existentes do artista consultado
  - [X] Armazenar o resultado em banco de dados NoSQL MongoDB 

- Minibiografia:  
  - [x] Obter a minibiografia do artista consultado
  - [x] Armazenar o resultado em banco de dados NoSQL MongoDB 


## 📋 Como executar o projeto
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/). 
Além disso, é recomendável utilizar um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/).
Para o uso da API do Discogs com todas as funcionalidades necessárioas para a execução pro projeto é necessário a geração de um token, para isso, deverá ser feito um cadastro no [site oficialn](https://www.discogs.com/developers)


### Instalação

1. Clone este repositório:

    ```bash
    git clone git@github.com:GeorgeDomingos/vinyl-hunter-API.git
    ```
2. Acesse a pasta do projeto no terminal/cmd:
    ```bash
    cd vinyl-hunter-API
    ```
3. Instale as bibliotecas necessárias:
   #### Flask:

    ```bash
    pip install Flask
    ```
    #### python-dotenv:
    ```bash
    pip install python-dotenv
    ```
     #### requests:
    ```bash
    pip install requests
    ```
     #### beautifulsoup4:
    ```bash
    pip install beautifulsoup4
    ```
    #### pandas:
    ```bash
    pip install pandas
    ```  
    #### pymongo:
    ```bash
    pip install pymongo
    ```      
        
5. Crie um arquivo chamado .env com todas as credenciais listadas no arquivo .env.example
   ```bash
   TOKEN= #inserir o token da API do Discogs
   PORT= #inserir o número da porta
   HOST= #inserir o nome do host
   MONGO_URI= #inserir a URI conforme o serviço MongoDB
   DB_NAME= #inserir o nome do banco de dados
   ```

6. Execute a aplicação


## 🛠 Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

As seguintes ferramentas foram usadas na construção do projeto:
- Python
- Flask
- Pandas
- Beautifulsoup4
- Pymongo
- MongoDB

## 📌 Endpoints da API
### Obter lista de discos de vinil:

**GET** `/vinyls`
- Este endpoint retorna uma lista de vinis para um artista específico.
- A requisição é feita com um objeto Json informando o nome do artista, conforme o exemplo:

    ```bash
    {
    "artist": "Jorge Ben Jor" //exemplo
    }
    ```
  #### Salvar consulta
  - Para salvar armazenar a consulta no banco de dados, usar o parâmetro 'save=db' na rota, conforme exemplo:
    ```bash
    {
    http://localhost:5000/vinyls?save=db
    }
    ```


### Obter minobiografia do artista:

**GET** `/minibio`

- Este endpoint retorna uma resumo das informações de um artista.
- A requisição é feita com um objeto Json informando o nome do artista, conforme o exemplo:
  
    ```bash
    {
    "artist": "Elza Soares" //exemplo
    }
    ```


## 🔎 Implementações futuras

- [ ] Incluir novas verificações
- [ ] Permitir a listagem de todas as versões de um álbum específico do artista
- [ ] Criar middlewares e funções utils
- [ ] Fazer o deploy da API 



## 📚 Referências
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) 
- [Pandas](https://pandas.pydata.org/docs/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [MongoDB](https://www.mongodb.com/docs/)
- [Discogs API](https://www.discogs.com/developers)
- [Git](https://git-scm.com/docs)


## 👨‍💻 Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/GeorgeDomingos"><img style="border-radius: 50%;" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" width="100px;" alt=""/><br /><sub><b>George Domingos</b></sub></a><br/></td>

  </tr>
</table>



![tech(1)](https://github.com/GeorgeDomingos/semsufoco-controle-financeiro-API-REST/assets/136137653/64bd7b09-21b7-43d3-9dc9-446ade2d35d8)
