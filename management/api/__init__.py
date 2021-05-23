from flask import Blueprint
from management import models
# from management.models import Permission

route_api = Blueprint('api_page', __name__)

from management.api.api import  *

#
# @route_api.app_context_processor
# def inject_permissions():
#     return dict(Permission=Permission)
