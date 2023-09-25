import logging
from functools import wraps
from urllib.parse import urljoin

import requests
from flask import request
from requests import JSONDecodeError

from swagger_server import db, config
from swagger_server.models import Zone
from swagger_server.models.sql_models import SAZone

logger = logging.getLogger('connexion.app')


def zone_endpoint(function):
    """
    This decorator will forward the request to the dedicated endpoint related to the zone. If the current endpoint is
    managing the zone, the request will not be forward and the code flow will continue. If the request goes need to be
    forward again, the script will raise an error to avoid infite loop
    :param function:
    :return:
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        zone_id = kwargs['zone_id']

        zone = db.session.query(SAZone).filter(SAZone.id == zone_id).one_or_none()
        if zone is None:
            return {'error': 'This zone does not exist'}, 404

        if zone.region.name != config.get_managed_region():

            if request.headers.get('FORWARDED_FROM', None) is not None:
                logger.error('This request have already been forward from another service')
                return {"error": "Error while routing the request, please contact admin"}, 500

            logger.info('This request is not managed by this endpoint')
            headers = {header[0]: header[1] for header in request.headers}
            headers['FORWARDED_FROM'] = config.get_managed_region()

            url = urljoin(zone.region.endpoint, request.path)
            logger.info(f'Forward request to {url}')

            forward_req = requests.Request(method=request.method, url=url, cookies=request.cookies,
                                           headers=headers, params=request.args)
            if request.is_json:
                forward_req.json = request.json
            res = requests.Session().send(forward_req.prepare())

            try:
                return res.json(), res.status_code
            except JSONDecodeError:
                return res.text, res.status_code

        del kwargs['zone_id']
        return function(zone=Zone.from_sa(sa_zone=zone), **kwargs)  # Make the zone model as first argument

    return wrapper
