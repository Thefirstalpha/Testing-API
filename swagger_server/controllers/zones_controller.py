from swagger_server.__main__ import db
from swagger_server.models.record import Record  # noqa: E501
from swagger_server.models.sql_models import SAZone
from swagger_server.models.zone import Zone  # noqa: E501

def get_zone_by_id(zone_id):  # noqa: E501
    sa_zone = db.session.query(SAZone).filter(SAZone.id == zone_id).one_or_none()
    if sa_zone is None:
        return {'error':'cannot find zone'}, 404
    return Zone.from_sa(sa_zone).to_dict()





def list_zones(name=None):  # noqa: E501
    query = db.session.query(SAZone)
    if name is not None:
        query = query.filter(SAZone.name == name)
    sa_zones = query.all()

    zones = [Zone.from_sa(sa_zone) for sa_zone in sa_zones]
    return zones
