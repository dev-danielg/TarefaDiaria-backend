from services import TarefaService
from repositories import TarefaRepository
from flask import request
from flask_jwt_extended import get_jwt_identity


class TarefaController:
    
    def __init__(self, repository: TarefaRepository, service: TarefaService) -> None:
        self.repository = repository
        self.service = service
    
    def cadastrar(self) -> tuple[dict[str, str | object], int]:
        try:
            tarefa = self.service.cadastrar(request.get_json(), int(get_jwt_identity()))
            
        except ValueError as e:
            return {
                "success": False,
                "message": str(e)
            }, 400
            
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }, 500
        
        return {
            "success": True,
            "message": "Tarefa criada com sucesso.",
            "data": {
                "id": tarefa.id,
                "usuario_id": tarefa.id_usuario,
                "titulo": tarefa.titulo,
                "descricao": tarefa.descricao,
                "concluida": tarefa.concluida
            }
        }, 201
        