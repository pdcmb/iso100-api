from flask import Blueprint, request
from api.model.camera import Camera
from api.schema.camera import CameraSchema
import logging

camera_api = Blueprint('camera_api', __name__)

@camera_api.route('/camera/<id>', methods=['GET'])
def get_camera(id=0):
    if id is None:
        result = Camera.query.all()
    else:
        result = Camera.query.get(id)
    return CameraSchema().jsonify(result)

@camera_api.route('/camera', methods=['POST'])
def add_camera():
    rq = request.json
    print(rq)
    return rq