from api import db
from api.model.producer import Producer
from api.model.mount import Mount
from api.model.sensor_format import SensorFormat

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), nullable=False)
    iso_min = db.Column(db.Integer, nullable=False)
    iso_max = db.Column(db.Integer, nullable=False)
    resolution =  db.Column(db.Float, nullable=False)
    autofocus = db.Column(db.Integer, nullable=False)
    ois = db.Column(db.Boolean, nullable=False)
    wr = db.Column(db.Boolean, nullable=False)
    wifi = db.Column(db.Boolean, nullable=False)
    weight =  db.Column(db.Float, nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id'), nullable=False)
    producer = db.relationship('Producer', backref=db.backref('cameras', lazy=True))
    sensor_format_id = db.Column(db.Integer, db.ForeignKey('sensor_format.id'), nullable=False)
    sensor_format = db.relationship('SensorFormat', backref=db.backref('cameras', lazy=True))
    mount_id = db.Column(db.Integer, db.ForeignKey('mount.id'), nullable=False)
    mount = db.relationship('Mount', backref=db.backref('cameras', lazy=True))

    def __init__(self, model, iso_min, iso_max, resolution, autofocus, ois, wr, wifi, weight,
        producer, sensor_format, mount):
            self.model = model
            self.iso_min = iso_min
            self.iso_max = iso_max
            self.resolution = resolution
            self.autofocus = autofocus
            self.ois = ois
            self.wr = wr
            self.wifi = wifi
            self.weight = weight
            self.producer = producer
            self.sensor_format = sensor_format
            self.mount = mount
            
