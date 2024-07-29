from typing import Optional
from pydantic import BaseModel as SCBaseModel
from pydantic import ConfigDict


#Schemas responsáveis pela serialização em Json do objeto tarefa
class TarefaSchema(SCBaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    titulo: str
    descricao: str
    status: str


