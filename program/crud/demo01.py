"""
python
"""

users = {
    1: {"name": "张三", "email": "zhangsan@qq.com"},
    2: {"name": "李四", "email": "lisi@qq.com"},
    3: {"name": "王五", "email": "wangwu@qq.com"}
}


def select_all():
    for index in users:
        print(f"用户信息：{users[index]}")


def get_user(user_id):
    if user_id not in users:
        print(f"user_id = {user_id} 不存在")
        return None
    return users[user_id]


def insert_user(user):
    next_id = max(users.keys()) + 1
    users[next_id] = user
    print(f"{user} 插入成功")


def update_user(user_id, user):
    if user_id not in users:
        print("此用户不存在")
    users[user_id] = user
    print(f"更新用户{user}成功")


def delete_user(user_id):
    if user_id not in users:
        print("此用户不存在")
    del users[user_id]
    print(f'user_id = {user_id}删除成功')


if __name__ == '__main__':
    select_all()
    user = {"name": "赵六", "email": "zhaoliu@qq.com"}
    insert_user(user)

    # 查询显示
    get_user(1)

    # 更新年龄
    user = {"name": "赵六11111", "email": "zhaoliu@qq.com"}
    update_user(1, user)

    # 删除用户
    delete_user(4)

    select_all()
