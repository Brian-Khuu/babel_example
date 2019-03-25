from flask import Flask, g, request
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
#    return request.accept_languages.best_match(['en', 'es'])
    return 'es'
from app import routes
