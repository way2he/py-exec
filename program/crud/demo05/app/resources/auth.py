from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from ..models import User
from ..schemas import AuthSchema

auth_schema = AuthSchema()


class AuthResource(Resource):
    def post(self):
        data = auth_schema.load(request.get_json())
        user = User.query.filter_by(name=data['name']).first()

        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        return {"message": "Invalid credentials"}, 401
