from flask import Flask

app = Flask(__name__)
app.secret_key = b"secret"
app.config['SECRET_KEY'] = 'secret'

from app import views
