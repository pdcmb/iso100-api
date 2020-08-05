from flask import Blueprint, request
from api import db
from api.model.mount import MountModel
from api.schema.mount import MountSchema

mount_api = Blueprint('mount_api', __name__)

@mount_api.route('/mount/', methods=['GET'])
def get_all_mounts():
    mounts = MountModel.query.all()
    return MountSchema(many=True).jsonify(mounts)

@mount_api.route('/mount/<int:id>', methods=['GET'])
def get_mount(id):
    mount = MountModel.query.get(id)
    return MountSchema().jsonify(mount)

@mount_api.route('/mount', methods=['POST'])
def add_mount():
    name = request.json['name']

    mount = MountModel(name=name)

    db.session.add(mount)
    db.session.commit()

    return MountSchema().jsonify(mount)

