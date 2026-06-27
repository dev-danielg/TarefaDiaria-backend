from models import Usuario
from repositories import UsuarioRepository
from werkzeug.security import generate_password_hash


class UsuarioService:
    
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository
    
    
    def cadastrar(self, dados: dict) -> Usuario:
        nome = dados.get("nome")
        email = dados.get("email")
        senha = dados.get("senha")
        
        if not nome or not senha or not email:
            raise ValueError("Nome, email e senha são obrigatórios.")
        
        usuario = self.repository.buscar_por_email(email)
        
        if usuario:
            raise ValueError("Usuário com mesmo email já cadastrado.")
        
        usuario = Usuario(nome=nome,
                          email=email,
                          senha_hash=generate_password_hash(senha))
        
        try:
            self.repository.cadastrar(usuario)
            self.repository.commit()
            return usuario
        
        except Exception:
            self.repository.rollback()
            raise
            
            
        
            
        
        
         