from sqlalchemy.orm import scoped_session
from models import Usuario
from sqlalchemy import select



class UsuarioRepository:
    
    def __init__(self, session: scoped_session) -> None:
        self.session = session
    
    
    def cadastrar(self, usuario: Usuario) -> None:
        self.session.add(usuario)
    
    
    def buscar_por_id(self, id: int) -> Usuario | None:
        query = select(Usuario).where(Usuario.id == id)
        return self.session.execute(query).scalar_one_or_none()


    def buscar_por_email(self, email: str) -> Usuario | None:
        query = select(Usuario).where(Usuario.email == email)
        return self.session.execute(query).scalar_one_or_none()
    
    
    def commit(self) -> None:
        self.session.commit()
    
    
    def rollback(self) -> None:
        self.session.rollback()