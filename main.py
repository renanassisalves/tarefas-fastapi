from fastapi import FastAPI

from core.configs import settings
from api.v1.api import apiRouter

app = FastAPI(title='Tarefas API - FastAPI + SQLAlchemy')
app.include_router(apiRouter, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app',
                host='0.0.0.0',
                port=8000,
                log_level='info',
                reload=True)
