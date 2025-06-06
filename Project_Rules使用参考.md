# Project Rules 使用参考

## 1. 规范文件结构

### 1.1 目录结构
```
project/
├── docs/
│   └── rules/                # 规范文件目录
│       ├── code_style.md     # 代码风格规范
│       ├── git_workflow.md   # Git 工作流规范
│       ├── testing.md        # 测试规范
│       └── security.md       # 安全规范
├── PROJECT_RULES.md         # 主规范文件
└── Project_Rules使用参考.md  # 本文档
```

### 1.2 规范文件说明
- `PROJECT_RULES.md`: 项目规范总览，包含其他规范的索引
- `code_style.md`: 代码风格和命名规范
- `git_workflow.md`: Git 工作流程和提交规范
- `testing.md`: 测试规范和最佳实践
- `security.md`: 安全规范和最佳实践

## 2. 规范使用指南

### 2.1 新项目初始化
1. 复制规范文件到项目目录
2. 根据项目需求调整规范内容
3. 确保团队成员了解规范
4. 配置相关工具支持

### 2.2 日常开发使用
1. 代码开发时参考 `code_style.md`
2. 提交代码时遵循 `git_workflow.md`
3. 编写测试时参考 `testing.md`
4. 安全相关操作参考 `security.md`

### 2.3 规范更新流程
1. 发现问题或需要改进
2. 团队讨论并达成共识
3. 更新相关规范文件
4. 通知团队成员
5. 更新工具配置

## 3. 最佳实践

### 3.1 规范执行
- 使用自动化工具强制执行规范
- 定期进行代码审查
- 保持文档同步更新
- 收集团队反馈

### 3.2 工具支持
- 代码检查：flake8, pylint, mypy
- 测试工具：pytest, coverage
- 安全工具：safety, pip-audit
- 文档工具：Sphinx, MkDocs

### 3.3 持续集成
- 配置 CI 流程
- 自动化测试
- 代码质量检查
- 安全漏洞扫描

### 3.4 规范执行
- 使用自动化工具强制执行规范
- 定期进行代码审查
- 收集团队反馈  

### 3.5 使用示例

#### 3.5.1 代码风格示例
```python
# 符合规范的函数定义
def calculate_total_price(items: list[dict], tax_rate: float) -> float:
    """
    计算商品总价（含税）
    
    Args:
        items: 商品列表，每个商品包含 price 和 quantity
        tax_rate: 税率
        
    Returns:
        float: 含税总价
    """
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    return subtotal * (1 + tax_rate)

# 符合规范的类定义
class OrderProcessor:
    """订单处理类"""
    
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate
        
    def process_order(self, order_id: str, items: list[dict]) -> dict:
        """处理订单"""
        total = calculate_total_price(items, self.tax_rate)
        return {
            'order_id': order_id,
            'total': total,
            'status': 'processed'
        }
```

#### 3.5.2 Git 工作流示例
```bash
# 1. 创建功能分支
git checkout -b feature/add-order-processing

# 2. 提交代码
git add .
git commit -m "feat: 添加订单处理功能

- 实现订单总价计算
- 添加订单处理类
- 添加单元测试"

# 3. 推送到远程
git push origin feature/add-order-processing

# 4. 创建 Pull Request
# 标题: feat: 添加订单处理功能
# 描述:
# - 功能说明
# - 测试覆盖
# - 相关文档
```

#### 3.5.3 测试规范示例
```python
# tests/test_order_processor.py
import pytest
from order_processor import OrderProcessor

def test_calculate_total_price():
    """测试总价计算"""
    items = [
        {'price': 100, 'quantity': 2},
        {'price': 50, 'quantity': 1}
    ]
    tax_rate = 0.1
    
    total = calculate_total_price(items, tax_rate)
    assert total == 275.0  # (200 + 50) * 1.1

def test_order_processor():
    """测试订单处理"""
    processor = OrderProcessor(tax_rate=0.1)
    order = processor.process_order(
        order_id="123",
        items=[{'price': 100, 'quantity': 1}]
    )
    
    assert order['order_id'] == "123"
    assert order['total'] == 110.0
    assert order['status'] == "processed"
```

#### 3.5.4 安全规范示例
```python
# 安全的密码处理
from passlib.hash import pbkdf2_sha256
import secrets

def hash_password(password: str) -> str:
    """安全地哈希密码"""
    salt = secrets.token_hex(16)
    return pbkdf2_sha256.hash(password + salt)

# 安全的API认证
from functools import wraps
from flask import request, abort
import jwt

def require_auth(f):
    """API认证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            abort(401)
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.InvalidTokenError:
            abort(401)
        return f(*args, **kwargs)
    return decorated
```

#### 3.5.5 文档规范示例
```python
# 模块级文档
"""
订单处理模块

该模块提供了订单处理相关的功能，包括：
- 订单总价计算
- 订单状态管理
- 订单处理流程

使用示例：
    processor = OrderProcessor(tax_rate=0.1)
    order = processor.process_order("123", [{'price': 100, 'quantity': 1}])
"""

# 函数文档
def validate_order(order: dict) -> bool:
    """
    验证订单数据
    
    Args:
        order: 订单数据字典，包含以下字段：
            - order_id: 订单ID
            - items: 商品列表
            - customer_id: 客户ID
            
    Returns:
        bool: 验证是否通过
        
    Raises:
        ValueError: 当订单数据格式不正确时
    """
    # 实现代码
    pass
```

## 4. 常见问题

### 4.1 规范冲突
- 记录冲突情况
- 团队讨论解决方案
- 更新规范文档
- 保持规范一致性

### 4.2 规范适应
- 根据项目特点调整
- 保持核心原则不变
- 定期评估规范效果
- 及时优化改进

### 4.3 团队协作
- 新成员培训
- 定期规范回顾
- 知识共享
- 经验总结

## 5. 规范维护

### 5.1 定期检查
- 规范适用性
- 工具支持情况
- 团队执行情况
- 问题收集整理

### 5.2 更新流程
1. 收集反馈
2. 分析问题
3. 制定方案
4. 更新文档
5. 通知团队

### 5.3 版本控制
- 规范文件版本管理
- 更新日志记录
- 变更说明
- 历史记录保存

## 6. 注意事项

### 6.1 规范执行
- 规范不是一成不变的
- 需要团队共同维护
- 保持规范实用性
- 避免过度规范

### 6.2 文档维护
- 及时更新文档
- 保持文档清晰
- 添加具体示例
- 定期检查链接

### 6.3 团队协作
- 及时沟通
- 互相学习
- 共同进步
- 知识共享

## 7. 参考资源

### 7.1 官方文档
- Python 官方文档
- Git 文档
- 测试框架文档
- 安全最佳实践

### 7.2 工具文档
- 代码检查工具
- 测试工具
- 安全工具
- 文档工具

### 7.3 社区资源
- 技术博客
- 开源项目
- 最佳实践
- 经验分享 