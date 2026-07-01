from flask import Blueprint
from repositories import UsuarioRepository
from services import AuthService
from controllers import AuthController
from extensions import db


bp = Blueprint("login", __name__, url_prefix="/api/auth")


@bp.route("/login", methods=["POST"])
def login():
    repository = UsuarioRepository(db.session)
    service = AuthService(repository)
    controller = AuthController(service)
    return controller.login()