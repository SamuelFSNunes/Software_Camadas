# Big Data Sandbox

Para versão em Inglês, click [aqui](../README.md)

Este projeto visa fornecer um ambiente sandbox para a aplicação de testes em big data. Ele consiste em um ambiente Docker com alguns containers contendo:

- Livy e Spark
- MinIO
- Zeppelin

Esses containers são configurados para se comunicarem entre si, permitindo a realização de trabalhos com big data.
.

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Resolução de Problemas](#resolução-de-problemas)
- [Desenvolverdores](#devs)

## Requisitos

- Docker instalado e configurado corretamente.
- Espaço livre em disco para os containers e dados gerados.
- Conexão com a internet para baixar imagens Docker e dependências durante a instalação inicial.

## Instalação

Siga os passos abaixo para instalar o projeto:

1. Clone este repositório para o seu ambiente local.

```bash
git clone https://github.com/SamuelFSNunes/Software_Camadas.git
```

2. Execute o comando de inicialização do Docker.

```bash
docker compose up --build
```

## Montagem

- Acessar o MinIO através do link (http://localhost:9001)
- Entra utilizando as seguintes credenciais
  - usuário: minioadmin
  - senha: minioadmin
- Acessar a aba Bucket e ciclar em **create bucket**
- Em bucket name digitar `warehouse` e selecionar **create bucket**

## Configuração

Após a instalação, o ambiente será configurado automaticamente. Você pode acessar os seguintes serviços:

- MinIO: [http://localhost:9001](http://localhost:9000)
- Zeppelin: [http://localhost:8080](http://localhost:8080)

## Resolução de Problemas

Se os serviços não estiverem funcionando conforme esperado, siga estas etapas de solução de problemas:

1. Verifique se o Docker está em execução.
2. Verifique os logs dos containers para mensagens de erro.
3. Reinicie os containers usando o comando `docker compose restart`.

## Devs

Este projeto é mantido por:

- Erick M. Cassoli - [GitHub](https://github.com/ErickCassoli)
- Vinicius Antunes - [GitHub](https://github.com/viniciusantunes26)
- Rafael Mattos - [GitHub](https://github.com/RafaMattss)
