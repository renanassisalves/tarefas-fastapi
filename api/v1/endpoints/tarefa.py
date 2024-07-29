from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tarefa_model import TarefaModel
from schemas.tarefa_schema import TarefaSchema
from core.deps import getSession
import logging

router = APIRouter()

# Método post
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TarefaSchema)
async def postTarefa(tarefa: TarefaSchema, db: AsyncSession = Depends(getSession)):
    novaTarefa = TarefaModel(titulo=tarefa.titulo,
                             descricao=tarefa.descricao,
                             status=tarefa.status)

    db.add(novaTarefa)
    await db.commit()

    return novaTarefa

# Método get de todas as tarefas
@router.get('/', response_model=List[TarefaSchema])
async def getTarefas(db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(TarefaModel)
        result = await session.execute(query)
        tarefas: List[TarefaModel] = result.scalars().all()

        return tarefas

# Método get de uma tarefa específica
@router.get('/{tarefaId}', response_model=TarefaSchema, status_code=status.HTTP_200_OK)
async def getTarefa(tarefaId: int, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == tarefaId)
        resultado = await session.execute(query)
        tarefa = resultado.scalar_one_or_none()

        if tarefa:
            return tarefa;
        else:
            raise HTTPException(detail='Tarefa não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)

# Método put para atualização de uma tarefa específica
@router.put('/{tarefaId}', response_model=TarefaSchema, status_code=status.HTTP_202_ACCEPTED)
async def putTarefa(tarefaId: int, tarefa: TarefaSchema, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == tarefaId)
        resultado = await session.execute(query)
        tarefaUpdate = resultado.scalar_one_or_none()

        if tarefaUpdate:
            tarefaUpdate.titulo = tarefa.titulo
            tarefaUpdate.descricao = tarefa.descricao
            tarefaUpdate.status = tarefa.status

            await session.commit()

            return tarefaUpdate
        else:
            raise HTTPException(detail='Tarefa não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)

# Método delete de uma tarefa específica
@router.delete('/{tarefaId}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteTarefa(tarefaId: int, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(TarefaModel).filter(TarefaModel.id == tarefaId)
        resultado = await session.execute(query)
        tarefaDelete = resultado.scalar_one_or_none()

        if tarefaDelete:
            await session.delete(tarefaDelete)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Tarefa não encontrada.',
                                status_code=status.HTTP_404_NOT_FOUND)