from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

users = {
    1: {"name": "张三", "email": "zhangsan@example.com"},
    2: {"name": "李四", "email": "lisi@example.com"}
}


class UserAPI(Resource):
    def get(self, user_id):
        if user_id not in users:
            abort(404, message=f"用户 {user_id} 不存在")
        return users[user_id]

    def delete(self, user_id):
        if user_id not in users:
            abort(404, message=f"用户 {user_id} 不存在")
        del users[user_id]
        return '', 204


api.add_resource(UserAPI, '/api/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
