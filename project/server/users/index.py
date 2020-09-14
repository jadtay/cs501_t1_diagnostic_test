# project/server/users/index.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users_blueprint = Blueprint('users', __name__)

class IndexAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
        users = User.query.with_entities(User.email)
        index = []
        for user in users:
            index.append(user)
        return make_response(jsonify(index))

# define the API resources
index_view = IndexAPI.as_view('index_api')

# add Rules for API Endpoints
users_blueprint.add_url_rule(
    '/users/index',
    view_func=index_view,
    methods=['POST', 'GET']
)