from blog import ma
from marshmallow import Schema, fields

class IdSchema(ma.Schema):
    id = fields.Int()


class NameFileSchema(ma.Schema):
    name_file=fields.Str()
