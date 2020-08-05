from flask import Blueprint, request
from api import db
from api.model.mount import MountModel
from api.schema.mount import MountSchema

sensor_api = Blueprint('sensor_api', __name__)