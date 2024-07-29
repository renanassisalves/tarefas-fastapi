from core.configs import settings
from sqlalchemy import Column, Integer, String

#Model do objeto tarefa
class TarefaModel(settings.DBBaseModel):
    __tablename__ = 'tarefas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(50))
    descricao: str = Column(String(100))
    status: str = Column(String(25))