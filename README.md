# Minha API CRUD - MVP

Este projeto é um MVP (Minimum Viable Product) da Disciplina Desenvolvimento Full Stack Básico da PUCRIO.

## Introdução
Esse é o back-end do sistema, que complementa o front-end representado pelo gerenciador de usuários desenvolvido no projeto. O back-end fornece os dados necessários para o funcionamento do [front-end](https://github.com/Levickl/1_MVP_Front-end), permitindo ao usuário interagir de forma eficaz com a aplicação.

O objetivo principal deste back-end é fornecer uma API para suportar as operações de CRUD (Create, Read, Update, Delete) necessárias para gerenciar os recursos de usuários. Durante o desenvolvimento, foi possivel implementar mais de 4 rotas.

## Como executar

Para executar este projeto, é necessário ter todas as bibliotecas Python listadas no arquivo ``requisitos.txt`` instaladas. Recomenda-se o uso de ambientes virtuais, como o [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) do Python, para isolar as dependências do projeto.


### Instalação das dependências

No diretório da API, execute o seguinte comando para instalar as dependências:

```
(env)$ pip install -r requisitos.txt
```

### Execução da API

Após instalar as dependências, você pode iniciar a API. Utilize o seguinte comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Uma vez que a API esteja em execução, abra o navegador e acesse [http://localhost:5000/#/](http://localhost:5000/#/) para verificar o status da API.
