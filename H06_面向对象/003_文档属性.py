class User:
    """系统用户类

    Attributes:
        username (str): 用户名
        is_active (bool): 用户是否激活
    """
    def __init__(self, username: str, is_active: bool = True):
        self.username = username
        self.is_active = is_active

print(User.__doc__)