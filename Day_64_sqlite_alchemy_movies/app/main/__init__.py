from flask import Blueprint, render_template, request, redirect, url_for

from ..repositories import movie_repo
from ..formsWTF import AddMovieForm, UpdateMovieForm
from ..external_api.moviedb import MovieDBService

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    # movie_repo.add_avatar()
    # movie_repo.add_phone_booth()
    movies = list(movie_repo.get_all_movies())
    return render_template(
        "index.html",
        movies=movies,
        enumerate=enumerate,
        reversed=reversed,
        list=list
    )


@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    movie_id = request.args.get('movie_id')
    form = UpdateMovieForm(movie_id=movie_id)
    if form.validate_on_submit():
        movie_repo.update_movie(
            form.movie_id.data,
            form.rating.data,
            form.review.data,
        )
        return redirect('/')
    return render_template(
        "edit.html",
        form=form
    )


@bp.route('/delete')
def delete():
    movie_id = int(request.args.get('movie_id'))
    movie_repo.delete_movie_by_id(movie_id)
    return redirect('/')


@bp.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        mdb_service = MovieDBService()
        mdb_service.set_movie_title(movie_title)
        movies = mdb_service.find_movies()
        return render_template("select.html", movies=movies.get('movies'))
    return render_template("add.html", form=form)


@bp.route('/find')
def find():
    mdb_movie_id = request.args.get('mdb_movie_id')
    mdb_service = MovieDBService()
    movie = mdb_service.get_movie(mdb_movie_id)
    new_movie_id = movie_repo.add_movie_to_db(movie)
    print(new_movie_id)
    return redirect(url_for('main.edit', movie_id=new_movie_id))
