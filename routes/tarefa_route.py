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
def buscar_todos():
    repository = TarefaRepository(db.session)
    service = TarefaService(repository)
    controller = TarefaController(repository, service)
    return controller.buscar_todos()


@bp.route("/<int:id_tarefa>", methods=["DELETE"])
@jwt_required()
def deletar(id_tarefa: int):
    repository = TarefaRepository(db.session)
    service = TarefaService(repository)
    controller = TarefaController(repository, service)
    return controller.deletar(id_tarefa)


@bp.route("/<int:id_tarefa>", methods=["PUT"])
@jwt_required()
def atualizar(id_tarefa: int):
    repository = TarefaRepository(db.session)
    service = TarefaService(repository)
    controller = TarefaController(repository, service)
    return controller.atualizar(id_tarefa)