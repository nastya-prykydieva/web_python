from flask import Blueprint
from app.todo.models import Todo

api_bp = Blueprint("api", __name__)

from . import views