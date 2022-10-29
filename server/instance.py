from flask import Flask, Blueprint
from flask_restplus import Api


class Server:
    def __init__(
        self,
    ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint("api", __name__, url_prefix="/Throwing-Tomatoes")
        self.api = Api(self.blueprint, doc="/doc", title="Rest Api Documentation")
        self.app.register_blueprint(self.blueprint)

        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://data.db"
        self.app.config["PROPAGATE_EXCEPTIONS"] = True
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIOS"] = False

        self.movies_ns = self.movies_ns()

        def movies_ns(
            self,
        ):
            return self.api.namespace(
                name="Movies", description="movies related operations", path="/"
            )

        def run(
            self,
        ):
            self.app.run(port=5000, debug=True, host="0.0.0.0")


server = Server()
