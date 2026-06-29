from services import UsuarioService
from repositories import UsuarioRepository
from flask import request
from flask_jwt_extended import get_jwt_identity


class UsuarioController:
    
    def __init__(self, repository: UsuarioRepository, service: UsuarioService) -> None:
        self.repository = repository
        self.service = service
        
    def cadastrar(self) -> tuple[dict[str, str | object], int]:
        try:
            usuario = self.service.cadastrar(request.get_json())
        
        except ValueError as e:
            return {
                "success": False,
                "message": str(e)
            }, 400
        
        except Exception:
            return {
                "success": False,
                "message": "Erro interno no servidor."
            }, 500
        
        return {
            "success": True,
            "message": "Usuário cadastrado com sucesso.",
            "data": {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email
            }
        }, 201
        