from flask import jsonify
from marshmallow import ValidationError

from ma import ma
from db import db
from controllers.movie_controller import Movie, MovieList, movie_ns

from server.instance import server

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Movie, "/movies/<int:id>")
api.add_resource(MovieList, "/movies")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    server.run()
