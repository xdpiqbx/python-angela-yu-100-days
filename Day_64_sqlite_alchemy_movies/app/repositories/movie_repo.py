from ..models.movie import Movie
from app.extensions import db
import sqlalchemy as sa
from ..MoviesDTO.chosen_movie import ChosenMovie


# Movie Repository

def get_all_movies():
    return db.session.execute(
        sa.select(Movie).order_by(Movie.rating.desc())
    ).scalars()


def delete_movie_by_id(movie_id: int):
    movie_to_delete: Movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()


def update_movie(movie_id: int, rating, review):
    movie_to_update: Movie = db.get_or_404(Movie, movie_id)
    movie_to_update.rating = rating
    movie_to_update.review = review
    db.session.commit()


def add_movie_to_db(movie: ChosenMovie) -> int:
    new_movie: Movie = Movie(
        title=movie.title,
        year=int(movie.year),
        description=movie.description,
        ranking=movie.ranking,
        img_url=movie.img_url
    )
    db.session.add(new_movie)
    db.session.commit()
    return new_movie.id


def add_phone_booth():
    db.session.add(Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth,"
                    "pinned down by an extortionist's sniper rifle."
                    "Unable to leave or receive outside help, Stuart's negotiation with"
                    "the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    ))
    db.session.commit()


def add_avatar():
    db.session.add(Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film,"
                    "learn the story of the Sully family (Jake, Neytiri, and their kids),"
                    "the trouble that follows them, the lengths they go to keep each other safe,"
                    "the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    ))
    db.session.commit()
