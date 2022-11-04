from ma import ma
from models.movie_model import MovieModel


class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MovieModel
        load_instance = True
