# Api de Tarefas
Backend de serviço de tarefas feito em FastAPI.

## Instruções de execução
####1 - Instalar a versão do Python 3.9+
####2 - Criar um diretório para o projeto com venv
####3 - utilizar o comando pip install -r requirements.txt para a instalação das bibliotecas necessárias
####4 - Configurar o banco de dados na string "DB_URL" do arquivo ./core/configs.py utilizando essas informações: "postgresql+asyncpg://{usuario}:{senha}@{host}:{porta}/{banco}"
####5 - Rodar o código criar_tabelas para a criação das tabelas no banco
####6 - Rodar o arquivo main.py para a execução do servidor local Uvicorn

## Tecnologias utilizadas
- FastAPI
- SqlAlchemy
- Pydantic
- PostgreSQL

## Comandos curl para testes:

###GET de todas as tarefas:
```
curl  -X GET \
  'http://localhost:8000/api/v1/tarefas' \
  --header 'Accept: */*' \
```

###GET de uma tarefa específica:
Substituir {IdTarefa} pela tarefa desejada.
```
curl  -X GET \
  'http://localhost:8000/api/v1/tarefas/{IdTarefa}' \
  --header 'Accept: */*' \
```

###POST de uma tarefa:
```
curl  -X POST \
  'http://localhost:8000/api/v1/tarefas/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "titulo": "Nova tarefa",
  "descricao": "Descrição de nova tarefa",
  "status": "Pendente"
}'
```

###PUT de uma tarefa:
Substituir {IdTarefa} pela tarefa desejada.
```
curl  -X PUT \
  'http://localhost:8000/api/v1/tarefas/{IdTarefa}' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "titulo": "Tarefa atualizada",
    "descricao": "Descrição da tarefa",
    "status": "testado"
}'
```

###DELETE de uma tarefa:
Substituir {IdTarefa} pela tarefa desejada.
```
curl  -X DELETE \
  'http://localhost:8000/api/v1/tarefas/2' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)'
```