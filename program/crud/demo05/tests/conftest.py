import pytest
from app import create_app
from app.extensions import db
from app.models import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.app_context():
        db.create_all()
        test_user = User(username="testuser")
        test_user.set_password("testpass")
        db.session.add(test_user)
        db.session.commit()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_header(client):
    res = client.post('/auth/login', json={
        "username": "testuser",
        "password": "testpass"
    })
    return {'Authorization': f'Bearer {res.json["access_token"]}'}
