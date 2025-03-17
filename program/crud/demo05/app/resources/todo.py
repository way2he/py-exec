from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource

from ..extensions import db, limiter
from ..models import Todo
from ..schemas import TodoSchema, PaginatedSchema

todo_schema = TodoSchema()
paginated_schema = PaginatedSchema()


class TodoResource(Resource):
    decorators = [jwt_required(), limiter.limit("100/hour")]

    def get(self, todo_id=None):
        if todo_id:
            todo = Todo.query.get_or_404(todo_id)
            return todo_schema.dump(todo)

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        pagination = Todo.query.filter_by(user_id=current_user.id).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return paginated_schema.dump({
            'page': page,
            'per_page': per_page,
            'total': pagination.total,
            'items': [todo_schema.dump(item) for item in pagination.items]
        })

    def post(self):
        data = todo_schema.load(request.get_json())
        todo = Todo(**data, user_id=current_user.id)
        db.session.add(todo)
        db.session.commit()
        return todo_schema.dump(todo), 201

    def put(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        data = todo_schema.load(request.get_json(), partial=True)
        for key, value in data.items():
            setattr(todo, key, value)
        db.session.commit()
        return todo_schema.dump(todo)

    def delete(self, todo_id):
        todo = Todo.query.get_or_404(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return {'message': 'Todo deleted'}, 204
