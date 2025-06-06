# 安全规范

## 1. 代码安全

### 1.1 敏感信息处理
```python
# 错误示例
DB_PASSWORD = "my_secret_password"
API_KEY = "sk_live_123456789"

# 正确示例
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")
```

### 1.2 配置文件安全
```python
# config.py
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# 配置类
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
```

### 1.3 依赖包安全
- 定期更新依赖包
- 使用 `pip-audit` 检查安全漏洞
- 使用 `safety` 检查已知漏洞
- 锁定依赖版本

## 2. 数据安全

### 2.1 数据加密
```python
from cryptography.fernet import Fernet

class DataEncryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_data(self, data: str) -> bytes:
        """加密数据"""
        return self.cipher_suite.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data: bytes) -> str:
        """解密数据"""
        return self.cipher_suite.decrypt(encrypted_data).decode()
```

### 2.2 密码处理
```python
from passlib.hash import pbkdf2_sha256

def hash_password(password: str) -> str:
    """密码哈希"""
    return pbkdf2_sha256.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """验证密码"""
    return pbkdf2_sha256.verify(password, hashed)
```

### 2.3 数据备份
- 定期备份重要数据
- 使用加密备份
- 多地点存储
- 测试恢复流程

## 3. 访问控制

### 3.1 认证机制
```python
from functools import wraps
from flask import request, abort

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if not api_key or not verify_api_key(api_key):
            abort(401)
        return f(*args, **kwargs)
    return decorated
```

### 3.2 权限控制
```python
class Permission:
    READ = 0x01
    WRITE = 0x02
    ADMIN = 0x04

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def has_permission(self, permission):
        return self.permissions & permission == permission
```

### 3.3 会话管理
- 使用安全的会话机制
- 设置合理的会话超时
- 实现会话注销
- 防止会话固定攻击

## 4. 安全审计

### 4.1 日志记录
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger('security')
    handler = RotatingFileHandler(
        'security.log',
        maxBytes=10000000,
        backupCount=5
    )
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```

### 4.2 安全监控
- 监控异常访问
- 记录安全事件
- 设置告警机制
- 定期安全报告

## 5. 网络安全

### 5.1 HTTPS 配置
```python
# Flask 配置
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30)
)
```

### 5.2 安全头部
```python
from flask_talisman import Talisman

Talisman(app,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    content_security_policy={
        'default-src': "'self'",
        'img-src': "'self' data: https:",
        'script-src': "'self' 'unsafe-inline' 'unsafe-eval'",
    }
)
```

## 6. 安全最佳实践

### 6.1 输入验证
```python
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
```

### 6.2 错误处理
```python
def handle_error(error):
    """统一错误处理"""
    response = {
        "error": str(error),
        "status": "error"
    }
    return response, getattr(error, 'code', 500)
```

### 6.3 安全检查清单
- [ ] 定期更新依赖包
- [ ] 检查安全漏洞
- [ ] 审查访问日志
- [ ] 测试备份恢复
- [ ] 验证安全配置
- [ ] 更新安全文档 