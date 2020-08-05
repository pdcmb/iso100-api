from api import db

class SensorFormat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    width = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height