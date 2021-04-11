# beer-model

## Introdução

Este repositório realiza duas entregas:

1. Treinamento de um modelo de predição de IBU utilizando Jupyter Notebook que se encontra na pasta `notebooks`
2. Imagem Docker que implementa uma API desenvolvida em FastAPI para a produtização do modelo treinado.

## Treinamento do Modelo

As explicações necessárias estão no próprio notebook do treinamento.

## FastAPI

Para testes locais, idealmente seria criado um arquivo `.env` com as variáveis de ambiente para desenvolvimento, mas para fins de demonstração deve-se renomear o arquivo `.env.example` para `.env`:

```
git clone https://github.com/amenegola/beer-model.git
cd beer-model/
mv .env.example .env
```

Instale os pacotes necessários em um ambiente virtual apropriado:

```
pip install -r requirements.txt
```

### Teste da API sem docker

Execute o servidor web com o comando

```
uvicorn --host 0.0.0.0 --port 8000 app.main:app
```

### Teste da API com docker

Com Docker instalado

```
./build_image.sh
./run_docker.sh
```

### Teste da API 

Acesse `localhost:8000/docs` no Chrome para testar a API. Um grande benefício do FastAPI, além de ser mais rápido, e além de realizar checagem nos dados de entrada, é que a documentação é criada automaticamente, tanto para referência como para testes. Ao acessar a rota de documentação mencionada, a seguinte página é disponibilizada:

<img src="https://i.imgur.com/uDlYeF4.png">

Para autorizar a execução da rota de predição, clique no botão `Authorize` e adicione a chave de API `134740f4-1c3c-4dba-ad02-875809d2bf0b`

Após, clique na rota, e clique no botão executar.