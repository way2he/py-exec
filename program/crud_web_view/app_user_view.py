# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
DATABASE = 'database.db'

# 数据库连接工厂
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 以字典形式返回结果
    return conn

# 初始化数据库（命令行执行）
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print("数据库初始化完成")

# 数据库查询辅助函数
def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv if rv else None) if one else rv

# 路由部分
@app.route('/')
def index():
    users = query_db('SELECT * FROM users ORDER BY id DESC')
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        try:
            query_db('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                     (name, email, age))
            flash('用户添加成功', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('邮箱已存在，请使用其他邮箱', 'danger')
        except Exception as e:
            flash(f'操作失败：{str(e)}', 'danger')

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        try:
            query_db('UPDATE users SET name=?, email=?, age=? WHERE id=?',
                     (name, email, age, id))
            flash('用户更新成功', 'success')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('邮箱已存在，请使用其他邮箱', 'danger')
        except Exception as e:
            flash(f'更新失败：{str(e)}', 'danger')

    user = query_db('SELECT * FROM users WHERE id = ?', [id], one=True)
    return render_template('edit.html', user=user)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    try:
        query_db('DELETE FROM users WHERE id = ?', [id])
        flash('用户删除成功', 'success')
    except Exception as e:
        flash(f'删除失败：{str(e)}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
