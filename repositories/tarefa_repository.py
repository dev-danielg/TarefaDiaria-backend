from models import Tarefa
from sqlalchemy import select
from sqlalchemy.orm import scoped_session
from typing import Sequence


class TarefaRepository:
    
    def __init__(self, session: scoped_session) -> None:
        self.session = session
        
    
    def buscar_por_id(self, id: int) -> Tarefa | None:
        query = select(Tarefa).where(Tarefa.id == id)
        return self.session.execute(query).scalar_one_or_none()
    
    
    def buscar_todos(self) -> Sequence[Tarefa]:
        query = select(Tarefa)
        return self.session.execute(query).scalars().all()
    
    
    def cadastrar(self, tarefa: Tarefa) -> None:
        self.session.add(tarefa)
    
    
    def deletar(self, tarefa: Tarefa) -> None:
        self.session.delete(tarefa)
    
    
    def atualizar(self, tarefa: Tarefa) -> None:
        self.session.add(tarefa)
        