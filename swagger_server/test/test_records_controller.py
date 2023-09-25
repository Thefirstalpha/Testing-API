# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.record import Record  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecordsController(BaseTestCase):
    """RecordsController integration test stubs"""

    def test_create_record(self):
        """Test case for create_record

        Create records in zone
        """
        body = Record()
        response = self.client.open(
            '/api/v1//zones/{zone-id}/records'.format(zone_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_record(self):
        """Test case for delete_record

        Delete record
        """
        response = self.client.open(
            '/api/v1//zones/{zone-id}/records/{record-id}'.format(zone_id='38400000-8cf0-11bd-b23e-10b96e4ef00d', record_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
