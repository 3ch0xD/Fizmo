from flask import Flask, Blueprint, render_template, url_for
from flask_login import current_user, login_required
from .api.top_movie import showcase_movie, rounded_vote_average, overview
from .api.video import video_url

views = Blueprint("views", __name__)

# General Routes
@views.route("/home/")
@login_required
def home():
    return render_template("/views/home.html", style='home.css',showcase_movie=showcase_movie, vote_average=rounded_vote_average, overview=overview, id=showcase_movie['id'])

@views.route("/explore/")
def explore():
    return render_template("/views/explore.html")

@views.route("/@me/")
def me():
    return render_template("/views/me.html")


# Routes Related To Movies
@views.route("/movie/info/<id>/")
def movie_info(id):
    return render_template('/views/movie/movie_info.html')

@views.route("/movie/watch/<id>/")
def watch_movie(id):
    video_url = f"https://vidsrc.pro/embed/movie/{id}?theme=cf0b0e"
    return render_template('/views/movie/watch_movie.html', video=video_url, style='watch_movie.css')


#Routes Related To Tv Shows
@views.route("/tv/info/<id>/")
def tv_info(id):
    return render_template('/views/tv/tv_info.html')

@views.route("/tv/watch/<id>/")
def watch_tv(id):
    return render_template('/views/movie/watch_tv.html')