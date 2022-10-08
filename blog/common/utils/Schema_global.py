from blog import ma

class IdSchema(ma.Schema):
    class Meta:
        fields = ("id",)

