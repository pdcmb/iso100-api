from flask import Blueprint, request
from api import db
from api.model.camera import CameraModel
from api.schema.camera import CameraSchema


camera_api = Blueprint('camera_api', __name__)

@camera_api.route('/camera/', methods=['GET'])
def get_all_cameras(id):
    cameras = CameraModel.query.all()
    return CameraSchema().jsonify(cameras)

@camera_api.route('/camera/<int:id>', methods=['GET'])
def get_camera(id):
    camera = CameraModel.query.get(id)
    return CameraSchema().jsonify(camera)

@camera_api.route('/camera', methods=['POST'])
def add_camera():
    model = request.json['model']
    iso_min = request.json['iso_min']
    iso_max = request.json['iso_max']
    resolution = request.json['resolution']
    autofocus = request.json['autofocus']
    ois = request.json['ois']
    wr = request.json['wr']
    wifi = request.json['wifi']
    weight = request.json['weight']
    producer = request.json['producer']
    sensor_format = request.json['sensor_format']
    mount = request.json['mount']

    camera = CameraModel(
        model=model, 
        iso_min=iso_min,
        iso_max=iso_max,
        resolution=resolution,
        autofocus=autofocus,
        ois=ois,
        wr=wr,
        wifi=wifi,
        weight=weight,
        producer=producer,
        sensor_format=sensor_format,
        mount=mount)

    db.session.add(camera)
    db.session.commit()

    return CameraSchema().jsonify(camera)

@camera_api.route('/camera/<int:id>', methods=['PATCH'])
def update_camera(id):
    model = request.json['model']
    iso_min = request.json['iso_min']
    iso_max = request.json['iso_max']
    resolution = request.json['resolution']
    autofocus = request.json['autofocus']
    ois = request.json['ois']
    wr = request.json['wr']
    wifi = request.json['wifi']
    weight = request.json['weight']
    producer = request.json['producer']
    sensor_format = request.json['sensor_format']
    mount = request.json['mount']

    camera = CameraModel.query.get(id)

    camera.model = model
    camera.iso_min = iso_min
    camera.iso_max = iso_max
    camera.resolution = resolution
    camera.autofocus = autofocus
    camera.ois = ois
    camera.wr = wr
    camera.wifi = wifi
    camera.weight = weight
    camera.producer = producer
    camera.sensor_format = sensor_format
    camera.mount = mount

    db.session.add(camera)
    db.session.commit()

    return CameraSchema().jsonify(camera)

@camera_api.route('camera/<int:id>', methods=['DELETE'])
def delete_camera(id):
    camera = CameraModel.query.get(id)

    db.session.delete(camera)
    db.session.commit()

    return CameraSchema().jsonify(camera)
