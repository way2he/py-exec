# app.py
from flask import Flask
from flask_restful import Api
from web_api_user import UserResource, UserListResource

app = Flask(__name__)
api = Api(app)

# API路由
api.add_resource(UserListResource, '/api/v1/users')
api.add_resource(UserResource, '/api/v1/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
