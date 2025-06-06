# 代码风格规范

## Python 代码规范

### 1. 基本规范
- 遵循 PEP 8 标准
- 使用 4 个空格缩进
- 行长度限制：79 字符
- 使用 UTF-8 编码

### 2. 命名规范
```python
# 类名：使用 PascalCase
class UserManager:
    pass

# 函数和变量：使用 snake_case
def calculate_total():
    user_count = 0
    return user_count

# 常量：使用大写字母
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# 私有成员：使用下划线前缀
class Database:
    def __init__(self):
        self._connection = None
        self.__secret_key = "xxx"  # 双下划线表示强私有
```

### 3. 注释规范
```python
def process_data(data: list, threshold: int) -> bool:
    """
    处理数据并返回处理结果

    Args:
        data (list): 待处理的数据列表
        threshold (int): 处理阈值

    Returns:
        bool: 处理是否成功

    Raises:
        ValueError: 当数据格式不正确时
    """
    pass
```

### 4. 导入规范
```python
# 标准库导入
import os
import sys

# 第三方库导入
import requests
import pandas as pd

# 本地模块导入
from .utils import helper
from ..config import settings
```

### 5. 类型注解
```python
from typing import List, Dict, Optional

def get_user_info(
    user_id: int,
    include_private: bool = False
) -> Dict[str, Optional[str]]:
    pass
``` 