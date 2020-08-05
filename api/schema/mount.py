from api import ma
from api.model.mount import Mount

class MountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mount