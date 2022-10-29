from pkg_resources import cleanup_resources
from db import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    tomatoes = db.Column(db.Integer, nullable=False)

    def __init__(self, title, tomatoes):
        self.title = title
        self.tomatoes = tomatoes

    def __repr__(self):
        return f"Movie(title={self.title}, tomatoes={self.tomatoes})"

    def json(self):
        return {"title": self.title, "tomatoes": self.tomatoes}

    @classmethod
    def find_movie_by_name(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_movie_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all_movies(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
