from app import app
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/movies')
def movies():
	movies = [
	{'title': 'Alien', 'times': ['3:45', '5:00']}, {'title': 'Aliens','times': ['3:45', '5:00']}]
	return render_template("movies.html", movies=movies)
