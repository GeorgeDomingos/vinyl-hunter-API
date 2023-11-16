

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

O Vinyhunter foi desenvolvido como desafio do módulo de Introdução à Engenharia de Dados do Programa FAST - Formação Acelerada em Análise e visualização de Dados - CESAR School. O projeto foi criado para aplicar os conceitos de ETL (Extract, Transform e Load) e Web Scraping.

O projeto usa a API do Discogs como fonte de dados para extrair informações sobre os discos que possuam versões na mídia vinil exixtentes com base no artista consultado. Em uma segunda etapa, é feito o tratamento da consulta obtida e a formatação com as informações mais relevantes (id, título, gravadora, ano e formato e o país onde o disco foi produzido). Na última etapa, o resultado pode ser exibido em um formato JSON ou armazenado em banco de dados NoSQL MongoDB.

A Vinylhunter também permite ao usuário obter uma mini bigrafia do artista consultado. É feita uma consulta ao site da Wikipedia e com o uso da bilioteca Beatifulsoup é feito uma Web Scraping da tabela com as informações básicas do artista, o resultado é tratado e depois pode ser exibido em formato JSON ou armazenado em banco de dados NoSQL MongoDB.


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
Além disto é recomendável utilizar um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/).
A API do Discogs para um uso com todas as suas funcionalidades requer a geração de um token, um cadastro será necessário no [site oficialn](https://www.discogs.com/developers)


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
![](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

As seguintes ferramentas foram usadas na construção do projeto:
- Python
- Flask
- Pandas
- Beautifulsoup4
- Pymongo
- MongoDB

## 📌 Endpoints da API
### Cadastrar usuário:

**POST** `/usuario`
- Cria uma nova conta de usuário.
- A requisição é feita com um objeto Json informando o nome, email e senha do usuário, conforme o exemplo:

    ```bash
    {
    "nome": "Gilberto Gil", //exemplo
    "email": "gilbertogil@email.com", //exemplo
    "senha": "123456", //exemplo
    }
    ```


### Login:

**POST** `/login`

- Realiza o login do usuário com base nas credenciais fornecidas.
- A requisição é feita com um objeto Json informando email e senha do usuário, conforme o exemplo:
  
    ```bash
    {
    "email": "itamar_assumpcao@email.com", //exemplo
    "senha": "123456", //exemplo
    }
    ```

___
  > As rotas a seguir exigem o token de autenticação do usuário logado, a intormação deve se informada no header em formato Bearer Token
  > 
___

### Detalhar usuário:

**GET** `/usuario`

- Detalha os dados do usuário logado.

### Atualizar usuário:

**PUT** `/usuario`
- Atualiza os dados do usuário logado
- Analisa se o e-mail inserido está sendo utilizado por outro usuário e impede caso essa situação seja verificada
- A requisição é feita com um objeto Json informando nome, email ou senha do usuário, conforme o exemplo:
  
    ```bash
    {
    "nome": "Jorge Ben Jor", //exemplo
    "email": "jorge_ben@email.com", //exemplo
    "senha": "123456", //exemplo
    }
    ```
### Listar categorias:
**GET** `/categoria`
- Lista os nomes de todas as categorias de transações cadastradas na Sem$ufoco.

### Listar transações:
**GET** `/transacao`
- Lista todas as transações cadastradas do usuário.
- Poderá ser passado parâmetro tipo query para filtrar transações, conforme o exemplo:
  
  <pre>
    GET/transacao?filtro[]=roupas&filtro[]=salários
  </pre>

### Detalhar transações:
**GET** `/transacao/:id`
- Detalha uma transação específica a partir do seu id de cadastro;
- O id da transação deverá ser passado como parâmetro de rota.

### Cadastrar transação:
**POST** `/transacao`
- Registra uma nova transação.
- A requisição é feita com um objeto Json informando a descrição, valor, data, id da categoria e tipo, conforme o exemplo:

    ```bash
    {
    "descricao": "Salário", //exemplo
    "valor": 500000, //exemplo (valor em centavos)
    "data": "2022-03-24T15:30:00.000Z", //exemplo
    "categoria_id": 6,
    "tipo": "entrada 
    }
    ```
### Atualizar transação 
**PUT** `/transacao/:id`
- Atualiza uma transação cadastrada
- O id da transação deverá ser passado como parâmetro de rota.

### Excluir transação:
**DELETE** `/transacao/:id`
- Exclui uma transação cadastrada
- O id da transação deverá ser passado como parâmetro de rota.

### Obter extrato de transações:
**GET** `/transacao/extrato`
- Exibe o extrato financeiro do usuário.


## 🔎 Implementações futuras

- [ ] Incluir verificações para validação de entradas utilizando a biblioteca Joi
- [ ] Refatorar as querys utilizando a biblioteca QueryBuilder Knex
- [ ] Utilizar a biblioteca DotEnv para criação das variáveis de ambiente
- [ ] Fazer o deploy da API 



## 📚 Referências
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [Node.js](https://nodejs.org/pt-br/docs) 
- [Express](https://expressjs.com/pt-br/4x/api.html)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Node-postgres (pg)](https://node-postgres.com/)
- [Bcrypt](https://www.npmjs.com/package/bcrypt)
- [JSON Web Tokens](https://jwt.io/introduction)
- [Nodemon](https://www.npmjs.com/package/nodemon)
- [Git](https://git-scm.com/docs)


## 👨‍💻 Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/GeorgeDomingos"><img style="border-radius: 50%;" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" width="100px;" alt=""/><br /><sub><b>George Domingos</b></sub></a><br/></td>

  </tr>
</table>



![tech(1)](https://github.com/GeorgeDomingos/semsufoco-controle-financeiro-API-REST/assets/136137653/64bd7b09-21b7-43d3-9dc9-446ade2d35d8)
