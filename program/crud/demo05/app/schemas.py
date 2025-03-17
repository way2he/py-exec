from marshmallow import Schema, fields, validate


class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    completed = fields.Bool()
    created_at = fields.DateTime(dump_only=True)


class AuthSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class PaginatedSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()
    total = fields.Int()
    items = fields.List(fields.Dict())
