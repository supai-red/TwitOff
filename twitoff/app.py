"""Store application logic in app.py"""
from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .models import DB, User

load_dotenv()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)  # this allows us to read the name of the file as name
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')  # stored in .env
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Twitoff', users=users)

    return app
