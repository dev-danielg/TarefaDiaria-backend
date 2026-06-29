from repositories import UsuarioRepository
from services import UsuarioService
from controllers import UsuarioController
from flask import Blueprint
from extensions import db


bp = Blueprint("usuario", __name__, url_prefix="/api/usuarios")


@bp.route("", methods=["POST"])
def cadastrar():
    repository = UsuarioRepository(db.session)
    service = UsuarioService(repository)
    controller = UsuarioController(repository, service)
    return controller.cadastrar()