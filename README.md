# Desafio Banco do Brasil: User Image System
- Autor: Rodrigo Touriño Machado de Oliveira Lima
- Data: 2021-05-02

## Descrição

API para gerenciar imagens de usuários desenvolvida com FastAPI, PostgreSQL e Docker.

## Instruções de uso

1. Baixe o repositório:

```sh
$ git clone https://github.com/rodrigotlima/desafio-bb.git
```

2. Acesse o diretório raiz que contém o arquivo `docker-compose.yml` buildar as imagens e rodar os containers:

```sh
$ docker-compose up -d --build
```

3. Acesse o endereço [http://localhost/docs](http://localhost/docs) para verificar a documentação Swagger gerada automaticamente

4. Para testar a aplicação:

```sh
$ docker exec -t <nome_do_container_web> pytest
```
