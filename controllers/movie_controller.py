from flask import request
from flask_restplus import Resource, fields

from models.movie_model import MovieModel
from schemas.movie_schema import MovieSchema

from server.instance import server

movie_ns = server.movie_ns

ITEM_NOT_FOUND = "Movie not found."


movie_schema = MovieSchema()
movie_list_schema = MovieSchema(many=True)


item = movie_ns.model(
    "Movie",
    {
        "title": fields.String(description="Movie title"),
        "tomatoes": fields.Integer(default=0),
    },
)


class Movie(Resource):
    def get(self, id):
        movie_data = MovieModel.find_movie_by_id(id)
        if movie_data:
            return movie_schema.dump(movie_data), 200
        return {"message": ITEM_NOT_FOUND}, 404

    @movie_ns.expect(item)
    def put(self, id):
        movie_data = MovieModel.find_movie_by_id(id)
        movie_json = request.get_json()

        movie_data.tomatoes = movie_json["tomatoes"]
        movie_data.title = movie_json["title"]

        movie_data.save_to_db()
        return movie_schema.dump(movie_data), 200

    def delete(self, id):

        movie_data = MovieModel.find_movie_by_id(id)
        if movie_data:
            movie_data.delete_from_db()
            return "", 204
        return {"message", ITEM_NOT_FOUND}


class MovieList(Resource):
    def get(self):
        return movie_list_schema.dump(MovieModel.find_all_movies()), 200

    @movie_ns.expect(item)
    @movie_ns.doc("Create an item")
    def post(self):
        movie_json = request.get_json()
        movie_data = movie_schema.load(movie_json)

        movie_data.save_to_db()

        return movie_schema.dump(movie_data), 201
