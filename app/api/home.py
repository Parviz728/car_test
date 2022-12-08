from flask import Blueprint, render_template

home = Blueprint(name='home', url_prefix="/", import_name=__name__)


@home.route("/")
def index():
    return render_template('home.html')
