from flask import Flask
from models import Usuario, Tarefa
import os
from dotenv import load_dotenv
from extensions import db, jwt
from datetime import timedelta
from routes import bp_tarefa

app = Flask(__name__)


load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MYSQL_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)


db.init_app(app)
jwt.init_app(app)


with app.app_context():
    db.create_all()
    

app.register_blueprint(bp_tarefa)


if __name__ == "__main__":
    app.run(debug=True)
