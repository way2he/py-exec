# tests/test_todos.py
def test_create_todo(client, auth_header):
    res = client.post('/todos',
                      json={"title": "Test Todo"},
                      headers=auth_header
                      )
    assert res.status_code == 201
    assert res.json['title'] == "Test Todo"


def test_rate_limit(client, auth_header):
    for _ in range(101):
        res = client.get('/todos', headers=auth_header)
    assert res.status_code == 429
