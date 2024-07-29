from fastapi import APIRouter

from api.v1.endpoints import tarefa

# Roteador dos endpoints da api, pode ser utilizado para unificar todos os endpoints que forem implementados.
apiRouter = APIRouter()
apiRouter.include_router(tarefa.router, prefix='/tarefas', tags=["tarefas"])