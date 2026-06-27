from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer
from extensions import Base


class Usuario(Base):
    
    __tablename__ = "usuario"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(300), nullable=False)
    