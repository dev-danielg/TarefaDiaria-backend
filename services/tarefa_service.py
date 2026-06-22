from models import Tarefa
from repositories import TarefaRepository


class TarefaService:
    
    def __init__(self, repository: TarefaRepository) -> None:
        self.repository = repository
        
    
    def cadastrar(self, dados: dict, id_usuario: int):
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
            
        if not titulo:
            raise ValueError("Tarefa deve conter ao menos o título.")
        
        if descricao and not titulo:
            raise ValueError("Tarefa não pode ter descrição sem nenhum título.")
        
        tarefa = Tarefa(titulo=titulo,
                        descricao=descricao,
                        concluida=False,
                        usuario_id=id_usuario)
        
        try:
            self.repository.cadastrar(tarefa)
            self.repository.session.commit()
            return tarefa
        
        except Exception:
            self.repository.session.rollback()
            raise
        