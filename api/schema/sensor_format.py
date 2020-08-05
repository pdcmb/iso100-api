from api.schema import ma
from api.model.sensor_format import SensorFormat

class SensorFormatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SensorFormat