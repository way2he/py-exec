import sqlite3
from contextlib import contextmanager

DATABASE = '../../../sqlite/mySqlite.db'


@contextmanager
def get_db_connection():
    """获取数据库连接"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 返回字典格式数据
    try:
        yield conn
    finally:
        conn.close()


def query_db(query, args=(), one=False):
    """通用查询方法"""
    with get_db_connection() as conn:
        cursor = conn.execute(query, args)
        if one:
            return cursor.fetchone()
        else:
            return cursor.fetchall()

