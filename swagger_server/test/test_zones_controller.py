# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.record import Record  # noqa: E501
from swagger_server.models.zone import Zone  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

    def test_get_record_by_id(self):
        """Test case for get_record_by_id

        Find zone by id
        """
        response = self.client.open(
            '/api/v1//zones/{zone-id}/records/{record-id}'.format(zone_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', record_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone_by_id(self):
        """Test case for get_zone_by_id

        Find zone by id
        """
        response = self.client.open(
            '/api/v1//zones/{zone-id}'.format(zone_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_record(self):
        """Test case for list_record

        List records in zone
        """
        response = self.client.open(
            '/api/v1//zones/{zone-id}/records'.format(zone_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_zones(self):
        """Test case for list_zones

        List zones
        """
        query_string = [('name', 'test.com')]
        response = self.client.open(
            '/api/v1//zones',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
