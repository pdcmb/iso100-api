from flask import Blueprint, request
from api import db
from api.model.producer import ProducerModel
from api.schema.producer import ProducerSchema


producer_api = Blueprint('producer_api', __name__)

@producer_api.route('/producer/', methods=['GET'])
def get_all_producers():
    producers = ProducerModel.query.all()
    return ProducerSchema(many=True).jsonify(producers)

@producer_api.route('/producer/<int:id>', methods=['GET'])
def get_producer(id):
    producer = ProducerModel.query.get(id)
    return ProducerSchema().jsonify(producer)

@producer_api.route('/producer', methods=['POST'])
def add_producer():
    name = request.json['name']

    producer = ProducerModel(name)

    db.session.add(producer)
    db.session.commit()

    return ProducerSchema().jsonify(producer)

@producer_api.route('/producer/<int:id>', methods=['PATCH'])
def update_producer(id):
    name = request.json['name']

    producer = ProducerModel.query.get(id)

    producer.name = name

    db.session.add(producer)
    db.session.commit()

    return ProducerSchema().jsonify(producer)

@producer_api.route('/producer/<int:id>', methods=["DELETE"])
def delete_producer(id):
    producer = ProducerModel.query.get(id)

    db.session.delete(producer)
    db.session.commit()

    return ProducerSchema().jsonify(producer)