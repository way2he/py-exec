from http import HTTPStatus

from program.crud_web_api.application import app


# 全局错误处理
@app.errorhandler(500)
def handle_internal_error(e):
    return {'message': '服务器内部错误'}, HTTPStatus.INTERNAL_SERVER_ERROR