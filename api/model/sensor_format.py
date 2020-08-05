from api.model import db

class SensorFormat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(80), nullable=False)