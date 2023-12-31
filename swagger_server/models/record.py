# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from swagger_server import util
from swagger_server.models.base_model_ import Model


class Record(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str = None, name: str = None, value: str = None, type: str = None,
                 zoneId: str = None):  # noqa: E501
        """Record - a model defined in Swagger

        :param id: The id of this Record.  # noqa: E501
        :type id: str
        :param name: The name of this Record.  # noqa: E501
        :type name: str
        :param value: The value of this Record.  # noqa: E501
        :type value: str
        :param type: The type of this Record.  # noqa: E501
        :type type: str
        :param zone_id: The zone_id of this Record.  # noqa: E501
        :type zone_id: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'value': str,
            'type': str,
            'zoneId': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'value': 'value',
            'type': 'type',
            'zoneId': 'zoneId'
        }
        self._id = id
        self._name = name
        self._value = value
        self._type = type
        self._zoneId = zoneId

    @classmethod
    def from_dict(cls, dikt) -> 'Record':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Record of this Record.  # noqa: E501
        :rtype: Record
        """
        return util.deserialize_model(dikt, cls)

    @classmethod
    def from_sa(cls, sa_record) -> 'Record':
        """Returns the sa model as a model

        :param dikt: A dict.
        :type: dict
        :return: The Zone of this Zone.  # noqa: E501
        :rtype: Zone
        """
        record = Record()
        record.id = sa_record.id
        record.name = sa_record.name
        record.type = sa_record.type
        record.value = sa_record.value
        record.zoneId = sa_record.zone.id
        return record

    @property
    def id(self) -> str:
        """Gets the id of this Record.


        :return: The id of this Record.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Record.


        :param id: The id of this Record.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Record.


        :return: The name of this Record.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Record.


        :param name: The name of this Record.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self) -> str:
        """Gets the value of this Record.


        :return: The value of this Record.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Record.


        :param value: The value of this Record.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def type(self) -> str:
        """Gets the type of this Record.


        :return: The type of this Record.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Record.


        :param type: The type of this Record.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def zoneId(self) -> str:
        """Gets the zone_id of this Record.


        :return: The zone_id of this Record.
        :rtype: str
        """
        return self._zoneId

    @zoneId.setter
    def zoneId(self, zoneId: str):
        """Sets the zone_id of this Record.


        :param zone_id: The zone_id of this Record.
        :type zone_id: str
        """

        self._zoneId = zoneId
