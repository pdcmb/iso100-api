from api import ma
from api.model.camera import Camera

class CameraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Camera