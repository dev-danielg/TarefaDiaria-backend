from services import AuthService
from flask import request
from flask_jwt_extended import create_access_token


class AuthController:
    
    def __init__(self, service: AuthService) -> None:
        self.service = service
    
    
    def login(self) -> tuple[dict[str, str | object], int]:
        try:
            usuario = self.service.login(request.get_json())
            
        except ValueError as e:
            return {
                "success": False,
                "message": str(e)
            }, 401
            
        except Exception:
            return {
                "success": False,
                "message": "Erro interno no servidor."
            }, 500
        
        return {
            "success": True,
            "message": "Usuário logado com sucesso.",
            "data": {
                "usuario": usuario.nome,
                "email": usuario.email,
                "access_token": create_access_token(identity=str(usuario.id))
            }
        }, 200
        
        
        
