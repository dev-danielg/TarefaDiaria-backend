from flask import Blueprint
from controllers import TarefaController
from services import TarefaService
from repositories import TarefaRepository
from extensions import db
from flask_jwt_extended import jwt_required


bp = Blueprint("tarefa", __name__, url_prefix="/api/tarefas")


@bp.route("", methods=["POST"])
@jwt_required()
def cadastrar():
    repository = TarefaRepository(db.session)
    service = TarefaService(repository)
    controller = TarefaController(repository, service)
    return controller.cadastrar()


@bp.route("", methods=["GET"])
@jwt_required()
def buscar_todos():
    repository = TarefaRepository(db.session)
    service = TarefaService(repository)
    controller = TarefaController(repository, service)
    return controller.buscar_todos()