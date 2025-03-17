# app/utils/logger.py
import logging
from logging.handlers import RotatingFileHandler

from flask import request


def setup_logger(app):
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )

    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=1024*1024*10,
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(app.config['LOG_LEVEL'])

    app.logger.addHandler(file_handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])

    @app.after_request
    def log_request(response):
        app.logger.info(
            f"{request.method} {request.path} {response.status_code}"
            f" - {request.remote_addr}"
        )
        return response
