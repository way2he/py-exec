from flask import Flask, request
from flask_restful import Api, Resource, abort

from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)

# 初始化数据库
with app.app_context():
    db.create_all()


class UserResource(Resource):
    def get(self, user_id=None):
        """获取单个/全部用户"""
        if user_id:
            user = User.query.get(user_id)
            if not user:
                abort(404, message="User not found")
            return user.to_dict()
        else:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)

            # 分页查询
            pagination = User.query.paginate(
                page=page,
                per_page=per_page,
                error_out=False
            )

            return {
                'data': [u.to_dict() for u in pagination.items],
                'pagination': {
                    'total': pagination.total,
                    'pages': pagination.pages,
                    'current': pagination.page,
                    'per_page': pagination.per_page
                }
            }, 200

    def post(self):
        """创建用户"""
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            abort(400, message="Missing required fields")

        if User.query.filter_by(name=data['name']).first():
            abort(409, message="name already exists")

        new_user = User(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

    def put(self, user_id):
        """更新用户"""
        user = User.query.get(user_id)
        if not user:
            abort(404, message="User not found")

        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            abort(400, message="Missing required fields")

        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        if 'age' in data:
            user.age = data['age']

        db.session.commit()
        return user.to_dict()

    def delete(self, user_id):
        """删除用户"""
        user = User.query.get(user_id)
        if not user:
            abort(404, message="User not found")

        db.session.delete(user)
        db.session.commit()
        return '', 204


# 注册路由
api.add_resource(UserResource, '/api/users', '/api/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
