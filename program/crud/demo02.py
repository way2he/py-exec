import sqlite3
from sqlite3 import Error

"""
python + sqlite3
"""


# 连接数据库（不存在时自动创建）
def create_connection(db_file="../../sqlite/mySqlite.db"):
    """创建数据库连接"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"成功连接数据库, sqlite3模块版本：{sqlite3.version}, sqlite底层引擎版本：{sqlite3.sqlite_version}")
        return conn
    except Error as e:
        print(e)
    return conn


# 增：插入新用户
def insert_user(conn, name, email, age):
    """插入单条数据"""
    sql = '''INSERT INTO users(name, email, age) VALUES(?,?,?)'''
    cur = conn.cursor()
    try:
        cur.execute(sql, (name, email, age))
        conn.commit()
        print(f"插入成功，ID：{cur.lastrowid}")
    except Error as e:
        print(f"插入失败：{e}")


# 查：获取所有用户
def select_all(conn):
    """查询所有记录"""
    cur = conn.cursor()
    cur.execute("select * from main.users")
    rows = cur.fetchall()

    print("\n当前用户列表：")
    for row in rows:
        print(f"用户信息：{row}")


# 改：更新用户信息
def update_user(conn, user_id, new_age):
    """更新年龄"""
    sql = '''UPDATE users SET age = ? WHERE id = ?'''
    cur = conn.cursor()
    try:
        cur.execute(sql, (new_age, user_id))
        conn.commit()
        print(f"更新ID {user_id} 成功")
    except Error as e:
        print(f"更新失败：{e}")


# 删：删除用户
def delete_user(conn, user_id):
    """删除记录"""
    sql = 'DELETE FROM users WHERE id=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (user_id,))
        conn.commit()
        print(f"删除ID {user_id} 成功")
    except Error as e:
        print(f"删除失败：{e}")


def delete_user_by_name(conn, user_name):
    """删除记录"""
    sql = 'DELETE FROM users WHERE name=?'
    cur = conn.cursor()
    try:
        cur.execute(sql, (user_name,))
        conn.commit()
        print(f"删除姓名 {user_name} 成功")
    except Error as e:
        print(f"删除失败：{e}")


if __name__ == '__main__':
    # 初始化数据库连接
    conn = create_connection()

    if conn:
        # 插入初始数据
        insert_user(conn, "王五", " wangwu@qq.com", 25)
        insert_user(conn, "赵六", " zhaoliu@qq.com", 30)

        # 查询显示
        select_all(conn)

        # 更新年龄
        update_user(conn, 1, 99)
        select_all(conn)

        # 删除用户
        delete_user(conn, 3)
        delete_user_by_name(conn, "王五")
        delete_user_by_name(conn, "赵六")
        select_all(conn)

        # 关闭连接
        conn.close()
