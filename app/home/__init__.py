from flask import Blueprint

home_bp = Blueprint('home', __name__,
    template_folder="templates",
    static_folder='static',
    static_url_path='/home/static'
    )

from app.home import routes