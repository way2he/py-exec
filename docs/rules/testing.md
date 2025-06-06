# 测试规范

## 1. 测试类型

### 1.1 单元测试
- 测试覆盖率要求 > 80%
- 每个功能模块必须包含单元测试
- 测试用例命名清晰，表达测试目的

### 1.2 集成测试
- 测试模块间的交互
- 验证数据流和业务流程
- 模拟真实环境

### 1.3 端到端测试
- 测试完整业务流程
- 验证用户交互
- 检查系统集成

## 2. 测试规范

### 2.1 测试文件组织
```
tests/
├── unit/              # 单元测试
│   ├── test_auth.py
│   └── test_user.py
├── integration/       # 集成测试
│   ├── test_api.py
│   └── test_db.py
└── e2e/              # 端到端测试
    └── test_workflow.py
```

### 2.2 测试命名规范
```python
# 测试类命名
class TestUserAuthentication:
    pass

# 测试方法命名
def test_login_with_valid_credentials():
    pass

def test_login_with_invalid_password():
    pass
```

### 2.3 测试用例结构
```python
def test_user_registration():
    """
    测试用户注册功能
    """
    # 准备测试数据
    user_data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "valid_password"
    }
    
    # 执行测试
    result = register_user(user_data)
    
    # 验证结果
    assert result.success is True
    assert result.user_id is not None
```

## 3. 测试工具

### 3.1 测试框架
- pytest：主要测试框架
- unittest：标准库测试框架
- doctest：文档测试

### 3.2 测试工具
- coverage：测试覆盖率
- pytest-cov：pytest 覆盖率插件
- pytest-mock：模拟对象
- pytest-xdist：并行测试

### 3.3 测试配置
```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --verbose --cov=src --cov-report=html
```

## 4. 测试最佳实践

### 4.1 测试原则
- 测试应该是独立的
- 测试应该是可重复的
- 测试应该是快速的
- 测试应该是可维护的

### 4.2 测试数据
- 使用测试夹具（fixtures）
- 避免硬编码测试数据
- 使用工厂模式生成测试数据
- 清理测试数据

### 4.3 模拟和存根
```python
@pytest.fixture
def mock_db():
    """模拟数据库连接"""
    with patch('app.database.Database') as mock:
        yield mock

def test_get_user(mock_db):
    """测试获取用户信息"""
    mock_db.get_user.return_value = {
        'id': 1,
        'name': 'Test User'
    }
    result = get_user(1)
    assert result['name'] == 'Test User'
```

## 5. 测试报告

### 5.1 覆盖率报告
- 行覆盖率
- 分支覆盖率
- 函数覆盖率
- 语句覆盖率

### 5.2 测试报告格式
- HTML 报告
- XML 报告
- 控制台输出
- 持续集成集成

## 6. 持续集成

### 6.1 CI 配置
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

### 6.2 测试环境
- 开发环境
- 测试环境
- 预发布环境
- 生产环境 