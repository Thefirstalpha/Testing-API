import logging
import uuid

import connexion

from swagger_server import db
from swagger_server.controllers.decorators import zone_endpoint
from swagger_server.models import Zone
from swagger_server.models.record import Record  # noqa: E501
from swagger_server.models.sql_models import SARecord

logger = logging.getLogger('connexion.app')


@zone_endpoint
def create_record(zone: Zone, body=None):
    if connexion.request.is_json:
        body = Record.from_dict(connexion.request.get_json())  # noqa: E501
    body.id = uuid.uuid4()

    sa_record = SARecord()
    sa_record.id = body.id
    sa_record.name = body.name
    sa_record.type = body.type
    sa_record.value = body.value
    sa_record.zone_id = zone.id

    db.session.add(sa_record)
    db.session.commit()

    body.zoneId = zone.id
    return body.to_dict()


@zone_endpoint
def delete_record(zone: Zone, record_id):
    sa_record = db.session.query(SARecord).filter(SARecord.id == record_id, SARecord.zone_id == zone.id).one()
    db.session.delete(sa_record)
    db.session.commit()
    return '', 204


@zone_endpoint
def get_record_by_id(zone: Zone, record_id):
    sa_record = db.session.query(SARecord).filter(SARecord.id == record_id, SARecord.zone_id == zone.id).one_or_none()
    if sa_record is None:
        return {"error": "record not found"}, 404
    return Record.from_sa(sa_record)


@zone_endpoint
def list_record(zone):
    sa_records = db.session.query(SARecord).filter(SARecord.zone_id == zone.id).all()
    return [Record.from_sa(record).to_dict() for record in sa_records]
