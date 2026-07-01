from repositories import UsuarioRepository
from models import Usuario
from werkzeug.security import check_password_hash


class AuthService:
    
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository
    
    def login(self, dados: dict) -> Usuario:
        email = dados.get("email")
        senha = dados.get("senha")
        
        if not email or not senha:
            raise ValueError("Email e senha são obrigatórios")
        
        usuario = self.repository.buscar_por_email(email)
        
        if not usuario or not check_password_hash(usuario.senha_hash, senha):
            raise ValueError("Email ou senha inválidas.")
        
        return usuario
        
        
        
    
        
        
        
        
        
        
        
        
        
         