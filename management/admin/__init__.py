from flask import Blueprint

admin = Blueprint('admin', __name__)

# from management.admin.admin import  *
from . import views