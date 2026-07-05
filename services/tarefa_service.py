from models import Tarefa
from repositories import TarefaRepository
from typing import Sequence
from models import Tarefa


class TarefaService:
    
    def __init__(self, repository: TarefaRepository) -> None:
        self.repository = repository
    
    
    def cadastrar(self, dados: dict, id_usuario: int) -> Tarefa:
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
            
        if not titulo:
            raise ValueError("Tarefa deve conter ao menos o título.")

        
        tarefa = Tarefa(titulo=titulo,
                        descricao=descricao,
                        concluida=False,
                        id_usuario=id_usuario)
        
        try:
            self.repository.cadastrar(tarefa)
            self.repository.commit()
            return tarefa
        
        except Exception:
            self.repository.rollback()
            raise
        
        
    def buscar_todos(self, id_usuario: int) -> Sequence[Tarefa]:
        try:
            tarefas = self.repository.buscar_todos(id_usuario)
            return tarefas
        
        except Exception:
            raise
            