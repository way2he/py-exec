# app.py
from flask import request
from flask import Flask
from http import HTTPStatus
import sqlite3
from flask_restful import Resource, Api
from do_db import get_db

app = Flask(__name__)
api = Api(app)

# 数据验证工具
def validate_user_data(data):
    errors = {}
    if not data.get('name') or len(data['name']) < 2 or len(data['name']) > 80:
        errors['name'] = '姓名长度需在2-80个字符之间'
    if not data.get('email') or '@' not in data['email']:
        errors['email'] = '无效的邮箱格式'
    if 'age' in data and (not isinstance(data['age'], int) or data['age'] < 0 or data['age'] > 120):
        errors['age'] = '年龄需在0-120之间'
    return errors


# RESTful资源
class UserListResource(Resource):
    def get(self):
        """获取所有用户"""
        db = get_db()
        cur = db.execute('SELECT id, name, email, age FROM users ORDER BY id DESC')
        users = [dict(row) for row in cur.fetchall()]
        return {'data': users, 'count': len(users)}, HTTPStatus.OK

    def post(self):
        """创建新用户"""
        data = request.get_json()
        errors = validate_user_data(data)
        if errors:
            return {'message': '验证失败', 'errors': errors}, HTTPStatus.BAD_REQUEST

        try:
            db = get_db()
            cur = db.execute(
                'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                (data['name'], data['email'], data.get('age'))
            )
            db.commit()
            return {'id': cur.lastrowid}, HTTPStatus.CREATED
        except sqlite3.IntegrityError as e:
            if 'UNIQUE' in str(e):
                return {'message': '邮箱已存在'}, HTTPStatus.CONFLICT
            return {'message': '数据库错误'}, HTTPStatus.INTERNAL_SERVER_ERROR


class UserResource(Resource):
    def get_user(self, user_id):
        db = get_db()
        cur = db.execute('SELECT id, name, email, age FROM users WHERE id = ?', (user_id,))
        user = cur.fetchone()
        if not user:
            return None
        return dict(user)

    def get(self, user_id):
        """获取单个用户"""
        user = self.get_user(user_id)
        if not user:
            return {'message': '用户不存在'}, HTTPStatus.NOT_FOUND
        return user, HTTPStatus.OK

    def put(self, user_id):
        """更新用户"""
        user = self.get_user(user_id)
        if not user:
            return {'message': '用户不存在'}, HTTPStatus.NOT_FOUND

        data = request.get_json()
        errors = validate_user_data(data)
        if errors:
            return {'message': '验证失败', 'errors': errors}, HTTPStatus.BAD_REQUEST

        try:
            db = get_db()
            db.execute('''
                UPDATE users SET 
                    name = ?, 
                    email = ?, 
                    age = ? 
                WHERE id = ?
            ''', (data['name'], data['email'], data.get('age'), user_id))
            db.commit()
            return {'message': '更新成功'}, HTTPStatus.OK
        except sqlite3.IntegrityError as e:
            if 'UNIQUE' in str(e):
                return {'message': '邮箱已存在'}, HTTPStatus.CONFLICT
            return {'message': '数据库错误'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self, user_id):
        """删除用户"""
        db = get_db()
        cur = db.execute('DELETE FROM users WHERE id = ?', (user_id,))
        db.commit()
        if cur.rowcount == 0:
            return {'message': '用户不存在'}, HTTPStatus.NOT_FOUND
        return '', HTTPStatus.NO_CONTENT

# API路由
api.add_resource(UserListResource, '/api/v1/users')
api.add_resource(UserResource, '/api/v1/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)