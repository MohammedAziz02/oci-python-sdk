# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CopyObjectMetadataSummary(object):
    """
    Details of copied objects.
    """

    #: A constant which can be used with the resolution_action property of a CopyObjectMetadataSummary.
    #: This constant has a value of "CREATED"
    RESOLUTION_ACTION_CREATED = "CREATED"

    #: A constant which can be used with the resolution_action property of a CopyObjectMetadataSummary.
    #: This constant has a value of "RETAINED"
    RESOLUTION_ACTION_RETAINED = "RETAINED"

    #: A constant which can be used with the resolution_action property of a CopyObjectMetadataSummary.
    #: This constant has a value of "DUPLICATED"
    RESOLUTION_ACTION_DUPLICATED = "DUPLICATED"

    #: A constant which can be used with the resolution_action property of a CopyObjectMetadataSummary.
    #: This constant has a value of "REPLACED"
    RESOLUTION_ACTION_REPLACED = "REPLACED"

    def __init__(self, **kwargs):
        """
        Initializes a new CopyObjectMetadataSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param old_key:
            The value to assign to the old_key property of this CopyObjectMetadataSummary.
        :type old_key: str

        :param new_key:
            The value to assign to the new_key property of this CopyObjectMetadataSummary.
        :type new_key: str

        :param name:
            The value to assign to the name property of this CopyObjectMetadataSummary.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this CopyObjectMetadataSummary.
        :type identifier: str

        :param object_type:
            The value to assign to the object_type property of this CopyObjectMetadataSummary.
        :type object_type: str

        :param object_version:
            The value to assign to the object_version property of this CopyObjectMetadataSummary.
        :type object_version: str

        :param aggregator_key:
            The value to assign to the aggregator_key property of this CopyObjectMetadataSummary.
        :type aggregator_key: str

        :param name_path:
            The value to assign to the name_path property of this CopyObjectMetadataSummary.
        :type name_path: str

        :param time_updated_in_millis:
            The value to assign to the time_updated_in_millis property of this CopyObjectMetadataSummary.
        :type time_updated_in_millis: int

        :param resolution_action:
            The value to assign to the resolution_action property of this CopyObjectMetadataSummary.
            Allowed values for this property are: "CREATED", "RETAINED", "DUPLICATED", "REPLACED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resolution_action: str

        """
        self.swagger_types = {
            'old_key': 'str',
            'new_key': 'str',
            'name': 'str',
            'identifier': 'str',
            'object_type': 'str',
            'object_version': 'str',
            'aggregator_key': 'str',
            'name_path': 'str',
            'time_updated_in_millis': 'int',
            'resolution_action': 'str'
        }

        self.attribute_map = {
            'old_key': 'oldKey',
            'new_key': 'newKey',
            'name': 'name',
            'identifier': 'identifier',
            'object_type': 'objectType',
            'object_version': 'objectVersion',
            'aggregator_key': 'aggregatorKey',
            'name_path': 'namePath',
            'time_updated_in_millis': 'timeUpdatedInMillis',
            'resolution_action': 'resolutionAction'
        }

        self._old_key = None
        self._new_key = None
        self._name = None
        self._identifier = None
        self._object_type = None
        self._object_version = None
        self._aggregator_key = None
        self._name_path = None
        self._time_updated_in_millis = None
        self._resolution_action = None

    @property
    def old_key(self):
        """
        Gets the old_key of this CopyObjectMetadataSummary.
        Old key of the object from where the object was copied. For example a dataflow key within the project being copied.


        :return: The old_key of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._old_key

    @old_key.setter
    def old_key(self, old_key):
        """
        Sets the old_key of this CopyObjectMetadataSummary.
        Old key of the object from where the object was copied. For example a dataflow key within the project being copied.


        :param old_key: The old_key of this CopyObjectMetadataSummary.
        :type: str
        """
        self._old_key = old_key

    @property
    def new_key(self):
        """
        Gets the new_key of this CopyObjectMetadataSummary.
        New key of the object to identify the copied object. For example the new dataflow key.


        :return: The new_key of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._new_key

    @new_key.setter
    def new_key(self, new_key):
        """
        Sets the new_key of this CopyObjectMetadataSummary.
        New key of the object to identify the copied object. For example the new dataflow key.


        :param new_key: The new_key of this CopyObjectMetadataSummary.
        :type: str
        """
        self._new_key = new_key

    @property
    def name(self):
        """
        Gets the name of this CopyObjectMetadataSummary.
        Name of the object.


        :return: The name of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CopyObjectMetadataSummary.
        Name of the object.


        :param name: The name of this CopyObjectMetadataSummary.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this CopyObjectMetadataSummary.
        Object identifier.


        :return: The identifier of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CopyObjectMetadataSummary.
        Object identifier.


        :param identifier: The identifier of this CopyObjectMetadataSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def object_type(self):
        """
        Gets the object_type of this CopyObjectMetadataSummary.
        Object type.


        :return: The object_type of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this CopyObjectMetadataSummary.
        Object type.


        :param object_type: The object_type of this CopyObjectMetadataSummary.
        :type: str
        """
        self._object_type = object_type

    @property
    def object_version(self):
        """
        Gets the object_version of this CopyObjectMetadataSummary.
        Object version.


        :return: The object_version of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CopyObjectMetadataSummary.
        Object version.


        :param object_version: The object_version of this CopyObjectMetadataSummary.
        :type: str
        """
        self._object_version = object_version

    @property
    def aggregator_key(self):
        """
        Gets the aggregator_key of this CopyObjectMetadataSummary.
        Aggregator key


        :return: The aggregator_key of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._aggregator_key

    @aggregator_key.setter
    def aggregator_key(self, aggregator_key):
        """
        Sets the aggregator_key of this CopyObjectMetadataSummary.
        Aggregator key


        :param aggregator_key: The aggregator_key of this CopyObjectMetadataSummary.
        :type: str
        """
        self._aggregator_key = aggregator_key

    @property
    def name_path(self):
        """
        Gets the name_path of this CopyObjectMetadataSummary.
        Object name path.


        :return: The name_path of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._name_path

    @name_path.setter
    def name_path(self, name_path):
        """
        Sets the name_path of this CopyObjectMetadataSummary.
        Object name path.


        :param name_path: The name_path of this CopyObjectMetadataSummary.
        :type: str
        """
        self._name_path = name_path

    @property
    def time_updated_in_millis(self):
        """
        Gets the time_updated_in_millis of this CopyObjectMetadataSummary.
        time at which this object was last updated.


        :return: The time_updated_in_millis of this CopyObjectMetadataSummary.
        :rtype: int
        """
        return self._time_updated_in_millis

    @time_updated_in_millis.setter
    def time_updated_in_millis(self, time_updated_in_millis):
        """
        Sets the time_updated_in_millis of this CopyObjectMetadataSummary.
        time at which this object was last updated.


        :param time_updated_in_millis: The time_updated_in_millis of this CopyObjectMetadataSummary.
        :type: int
        """
        self._time_updated_in_millis = time_updated_in_millis

    @property
    def resolution_action(self):
        """
        Gets the resolution_action of this CopyObjectMetadataSummary.
        Object resolution action.

        Allowed values for this property are: "CREATED", "RETAINED", "DUPLICATED", "REPLACED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resolution_action of this CopyObjectMetadataSummary.
        :rtype: str
        """
        return self._resolution_action

    @resolution_action.setter
    def resolution_action(self, resolution_action):
        """
        Sets the resolution_action of this CopyObjectMetadataSummary.
        Object resolution action.


        :param resolution_action: The resolution_action of this CopyObjectMetadataSummary.
        :type: str
        """
        allowed_values = ["CREATED", "RETAINED", "DUPLICATED", "REPLACED"]
        if not value_allowed_none_or_none_sentinel(resolution_action, allowed_values):
            resolution_action = 'UNKNOWN_ENUM_VALUE'
        self._resolution_action = resolution_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
