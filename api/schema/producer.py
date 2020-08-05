from api import ma
from api.model.producer import Producer

class ProducerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producer