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
        
        
    def buscar_todos(self, titulo: str | None, concluida: str | int | None) -> Sequence[Tarefa]:
        titulo = titulo.strip() if titulo is not None and titulo != "" else None
        concluida = int(concluida) if concluida is not None and concluida != "" else None
        
        try:
            tarefas = self.repository.buscar_todos(titulo, concluida)
            return tarefas
        
        except Exception:
            raise
        
    
    def buscar_por_id(self, id_tarefa: int, id_usuario: int) -> Tarefa:
        tarefa = self.repository.buscar_por_id(id_tarefa)
        
        if not tarefa:
            raise LookupError("Tarefa específica não encontrada.")
        
        if tarefa.id_usuario != id_usuario:
            raise ValueError("Acesso negado.")
        
        try:
            return tarefa
        
        except Exception:
            raise
    
    
    def deletar(self, id_tarefa:int, id_usuario: int):
        tarefa = self.buscar_por_id(id_tarefa, id_usuario)
        
        try:
            self.repository.deletar(tarefa)
            self.repository.commit()
            return tarefa
        
        except Exception:
            self.repository.rollback()
            raise
        
    
    def atualizar(self, id_tarefa, id_usuario: int):
        tarefa = self.buscar_por_id(id_tarefa, id_usuario)
        
        try:
            self.repository.atualizar(tarefa)
            self.repository.commit()
            return tarefa
        
        except Exception:
            self.repository.rollback
            raise