from flask import Flask, render_template, redirect, Blueprint
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)

@albums_blueprint.route("/albums/<id>" )
def album_show(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album=album)

@albums_blueprint.route("/albums/<id>/delete", methods=["POST"])
def delete_task(id):
    album_repository.delete(id)
    return redirect("/albums")

    