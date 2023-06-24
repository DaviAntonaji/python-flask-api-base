# Projeto Base para APIs com Python e Flask 😁

Este projeto é uma base para o desenvolvimento de APIs utilizando Python e a biblioteca Flask. Ele permite a conexão com qualquer banco de dados SQL por meio da biblioteca SQLAlchemy.

## 👨🏻‍💻 Sobre o Projeto

O objetivo deste projeto é fornecer uma estrutura inicial para o desenvolvimento de APIs em Python. Ele inclui funcionalidades essenciais, como rotas, autenticação JWT e geração de tokens.

## 📦 Estrutura do Projeto

```
├── Dockerfile                  # Arquivo de configuração do Docker
├── LICENSE                     # Arquivo de licença
├── README.md                   # Documentação do projeto
├── app.py                      # Arquivo principal da aplicação Flask
├── requirements.txt            # Arquivo de dependências Python
├── sql_alchemy.py              # Arquivo de configuração do SQLAlchemy
└── auth                        # Diretório contendo arquivos relacionados à autenticação
    ├── cryptdecrypt.py         # Arquivo de gerenciamento de criptografia
    └── managertk.py            # Arquivo de gerenciamento de tokens
├── models                      # Diretório contendo arquivos de definição dos modelos de dados
├── tests                       # Diretório contendo arquivos de testes unitários
├── routes                      # Diretório contendo arquivos de definição das rotas da API
├── emails                      # Diretório contendo os templates de e-mails
├── resources                   # Diretório contendo funcionalides da aplicação
└── utils                       # Diretório contendo utilitários auxiliares
    ├── EmailsManagement.py     # Arquivo de gerenciamento de emails (pasta utils)
    ├── S3FileManagement.py     # Arquivo de gerenciamento de arquivos no S3 (pasta utils)
    └── webhooks.py             # Arquivo de gerenciamento de webhooks (pasta utils)
```

## 🧪 Testes Automatizados

Este projeto inclui testes automatizados para verificar o funcionamento correto da API. Os testes estão localizados no diretório `tests`. 

O teste `HealthCheck` é responsável por verificar se a API está funcionando corretamente. Ele realiza uma requisição GET ao endpoint de health check e verifica o status da resposta, a presença da propriedade "version" no JSON retornado e o tempo de resposta.

Para executar os testes automatizados, siga as etapas abaixo:

1. Certifique-se de que a aplicação esteja em execução.
2. Abra um terminal e navegue até o diretório do projeto.
3. Execute o seguinte comando para executar o teste:
```
python3 tests/health_check.py
```





## ⬇️ Instalação

Antes de começar, certifique-se de ter o Python 3.10.6 instalado em seu ambiente.

1. Clone este repositório para o seu ambiente local.
2. Acesse a pasta do projeto em um terminal.
3. Execute o seguinte comando para instalar as dependências:
```
pip install -r requirements.txt
```

4. Execute o seguinte comando para iniciar a aplicação:
```
python3 app.py
```

## 🐳 Docker
Este projeto também inclui um Dockerfile, permitindo o uso de containerização da aplicação. Siga as instruções abaixo para usar o Docker:

1. Certifique-se de ter o Docker instalado em seu ambiente.

2. Na pasta do projeto, execute o seguinte comando para buildar a imagem Docker:
```
docker build --build-arg PORT=5001 -t flaskapi . 
```

3. Depois que a imagem Docker for construída, você pode executar a aplicação em um contêiner Docker usando o seguinte comando:
```
docker run -d --restart=always --name flaskApi -p 5001:5001 -v $(pwd):/api flaskapi

```

Este comando realiza o seguinte:

* -d inicia o contêiner em segundo plano (modo "detached").
* --restart=always configura o contêiner para reiniciar automaticamente em caso de falhas ou reinicializações do sistema.
* --name flaskApi define o nome do contêiner como "flaskApi".
* -p 5001:5001 mapeia a porta 5001 do contêiner para a porta 5001 do seu host local, permitindo que você acesse a API.
* -v $(pwd):/api mapeia o volume do diretório atual para o diretório /api dentro do contêiner, garantindo que quaisquer alterações feitas no código sejam refletidas instantaneamente na aplicação em execução.



## ⚙️ Configurações

As configurações do projeto podem ser encontradas no arquivo `.env`. Nele, você poderá definir as credenciais de acesso ao banco de dados e outras variáveis de ambiente relevantes.

## 🙏  Contribuição

Se você quiser contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).