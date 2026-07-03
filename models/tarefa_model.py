from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Boolean, ForeignKey
from extensions import Base


class Tarefa(Base):
    
    __tablename__ = "tarefa"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    descricao: Mapped[str] = mapped_column(String(150), nullable=True)
    concluida: Mapped[bool] = mapped_column(Boolean, nullable=False)