from flask import Flask, Blueprint
from flask_restplus import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint("api", __name__, url_prefix="/Throwing-Tomatoes")
        self.api = Api(self.bluePrint, doc="/doc", title="Rest Api Documentation")
        self.app.register_blueprint(self.bluePrint)

        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
        self.app.config["PROPAGATE_EXCEPTIONS"] = True
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIOS"] = False

        self.movie_ns = self.movie_ns()

    def movie_ns(self):
        return self.api.namespace(
            name="Movies", description="movies related operations", path="/"
        )

    def run(self):
        self.app.run(port=5000, debug=True, host="0.0.0.0")


server = Server()
