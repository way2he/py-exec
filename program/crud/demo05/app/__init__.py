from flask import Flask
from flask_restful import Api

from .config import Config
from .extensions import db, jwt, limiter
from .resources.auth import AuthResource
from .resources.todo import TodoResource
from .utils.logger import setup_logger


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    setup_logger(app)

    # 注册API资源
    api = Api(app)
    api.add_resource(AuthResource, '/auth/login')
    api.add_resource(TodoResource, '/todos', '/todos/<int:todo_id>')

    # 全局异常处理
    @app.errorhandler(404)
    def handle_not_found(e):
        return {'error': str(e)}, 404

    @app.errorhandler(500)
    def handle_server_error(e):
        app.logger.error(f"Server Error: {str(e)}")
        return {'error': 'Internal server error'}, 500

    return app
