import sqlite3
from flask import Flask, request, jsonify, abort
from flask.views import MethodView
from models import query_db, get_db_connection

# 初始化应用
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # 禁止JSON自动排序


class UserAPI(MethodView):
    def get(self, user_id):
        """获取用户"""
        if user_id:
            # 单用户查询
            user = query_db('SELECT id, name, email, age FROM users WHERE id = ?', [user_id], one=True)
            if not user:
                abort(404, description="User not found")
            return jsonify(dict(user))
        else:
            # 列表查询
            users = query_db('SELECT * FROM users')
            return jsonify([dict(user) for user in users])

    def post(self):
        """创建用户"""
        data = request.json
        if not data or 'name' not in data or 'email' not in data:
            abort(400, description="Missing required fields: username or email")

        try:
            with get_db_connection() as conn:
                cursor = conn.execute('''
                    INSERT INTO users (name, email, age) VALUES (?, ?, ?)
                ''', (data['name'], data['email'], data['age']))
                conn.commit()
                new_id = cursor.lastrowid
                return jsonify({"id": new_id, **data}), 201
        except sqlite3.IntegrityError:
            abort(409, description="数据已存在")

    def put(self, user_id):
        """更新用户"""
        data = request.json
        if not data:
            abort(400, description="No data provided")

        user = query_db('SELECT * FROM users WHERE id = ?', [user_id], one=True)
        if not user:
            abort(404, description="User not found")

        updates = []
        params = []
        for key in ['username', 'email']:
            if key in data:
                updates.append(f"{key} = ?")
                params.append(data[key])

        if not updates:
            abort(400, description="No valid fields to update")

        params.append(user_id)
        try:
            with get_db_connection() as conn:
                conn.execute(f'''
                    UPDATE users 
                    SET {', '.join(updates)}
                    WHERE id = ?
                ''', params)
                conn.commit()
                return jsonify({"message": "更新成功：user_id = " + user_id}), 200
        except sqlite3.IntegrityError:
            abort(409, description="数据已存在")

    def delete(self, user_id):
        """删除用户"""
        user = query_db('SELECT * FROM users WHERE id = ?', [user_id], one=True)
        if not user:
            abort(404, description="User not found")

        with get_db_connection() as conn:
            conn.execute('DELETE FROM users WHERE id = ?', [user_id])
            conn.commit()
            return '', 204

# 注册路由
user_view = UserAPI.as_view('user_api')
app.add_url_rule('/api/users', view_func=user_view, methods=['GET', 'POST'])
app.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True)
