# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityDiscovered(object):
    """
    The details of the base entity discovery.
    """

    #: A constant which can be used with the discover_status property of a EntityDiscovered.
    #: This constant has a value of "PREV_DISCOVERED"
    DISCOVER_STATUS_PREV_DISCOVERED = "PREV_DISCOVERED"

    #: A constant which can be used with the discover_status property of a EntityDiscovered.
    #: This constant has a value of "NEW_DISCOVERED"
    DISCOVER_STATUS_NEW_DISCOVERED = "NEW_DISCOVERED"

    #: A constant which can be used with the discover_status property of a EntityDiscovered.
    #: This constant has a value of "NOT_FOUND"
    DISCOVER_STATUS_NOT_FOUND = "NOT_FOUND"

    #: A constant which can be used with the discover_status property of a EntityDiscovered.
    #: This constant has a value of "DISCOVERING"
    DISCOVER_STATUS_DISCOVERING = "DISCOVERING"

    #: A constant which can be used with the entity_type property of a EntityDiscovered.
    #: This constant has a value of "STORAGE_SERVER_DISCOVER_SUMMARY"
    ENTITY_TYPE_STORAGE_SERVER_DISCOVER_SUMMARY = "STORAGE_SERVER_DISCOVER_SUMMARY"

    #: A constant which can be used with the entity_type property of a EntityDiscovered.
    #: This constant has a value of "STORAGE_GRID_DISCOVER_SUMMARY"
    ENTITY_TYPE_STORAGE_GRID_DISCOVER_SUMMARY = "STORAGE_GRID_DISCOVER_SUMMARY"

    #: A constant which can be used with the entity_type property of a EntityDiscovered.
    #: This constant has a value of "DATABASE_SYSTEM_DISCOVER_SUMMARY"
    ENTITY_TYPE_DATABASE_SYSTEM_DISCOVER_SUMMARY = "DATABASE_SYSTEM_DISCOVER_SUMMARY"

    #: A constant which can be used with the entity_type property of a EntityDiscovered.
    #: This constant has a value of "INFRASTRUCTURE_DISCOVER_SUMMARY"
    ENTITY_TYPE_INFRASTRUCTURE_DISCOVER_SUMMARY = "INFRASTRUCTURE_DISCOVER_SUMMARY"

    #: A constant which can be used with the entity_type property of a EntityDiscovered.
    #: This constant has a value of "INFRASTRUCTURE_DISCOVER"
    ENTITY_TYPE_INFRASTRUCTURE_DISCOVER = "INFRASTRUCTURE_DISCOVER"

    def __init__(self, **kwargs):
        """
        Initializes a new EntityDiscovered object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ExternalStorageGridDiscoverySummary`
        * :class:`~oci.database_management.models.ExternalExadataInfrastructureDiscovery`
        * :class:`~oci.database_management.models.ExternalDatabaseSystemDiscoverySummary`
        * :class:`~oci.database_management.models.ExternalExadataInfrastructureDiscoverySummary`
        * :class:`~oci.database_management.models.ExternalStorageServerDiscoverySummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EntityDiscovered.
        :type id: str

        :param agent_id:
            The value to assign to the agent_id property of this EntityDiscovered.
        :type agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this EntityDiscovered.
        :type connector_id: str

        :param display_name:
            The value to assign to the display_name property of this EntityDiscovered.
        :type display_name: str

        :param version:
            The value to assign to the version property of this EntityDiscovered.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this EntityDiscovered.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this EntityDiscovered.
        :type status: str

        :param discover_status:
            The value to assign to the discover_status property of this EntityDiscovered.
            Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING"
        :type discover_status: str

        :param discover_error_code:
            The value to assign to the discover_error_code property of this EntityDiscovered.
        :type discover_error_code: str

        :param discover_error_msg:
            The value to assign to the discover_error_msg property of this EntityDiscovered.
        :type discover_error_msg: str

        :param entity_type:
            The value to assign to the entity_type property of this EntityDiscovered.
            Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER"
        :type entity_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'agent_id': 'str',
            'connector_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'discover_status': 'str',
            'discover_error_code': 'str',
            'discover_error_msg': 'str',
            'entity_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'agent_id': 'agentId',
            'connector_id': 'connectorId',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'discover_status': 'discoverStatus',
            'discover_error_code': 'discoverErrorCode',
            'discover_error_msg': 'discoverErrorMsg',
            'entity_type': 'entityType'
        }

        self._id = None
        self._agent_id = None
        self._connector_id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._discover_status = None
        self._discover_error_code = None
        self._discover_error_msg = None
        self._entity_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityType']

        if type == 'STORAGE_GRID_DISCOVER_SUMMARY':
            return 'ExternalStorageGridDiscoverySummary'

        if type == 'INFRASTRUCTURE_DISCOVER':
            return 'ExternalExadataInfrastructureDiscovery'

        if type == 'DATABASE_SYSTEM_DISCOVER_SUMMARY':
            return 'ExternalDatabaseSystemDiscoverySummary'

        if type == 'INFRASTRUCTURE_DISCOVER_SUMMARY':
            return 'ExternalExadataInfrastructureDiscoverySummary'

        if type == 'STORAGE_SERVER_DISCOVER_SUMMARY':
            return 'ExternalStorageServerDiscoverySummary'
        else:
            return 'EntityDiscovered'

    @property
    def id(self):
        """
        Gets the id of this EntityDiscovered.
        The `OCID`__ of the entity discovered.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this EntityDiscovered.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EntityDiscovered.
        The `OCID`__ of the entity discovered.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this EntityDiscovered.
        :type: str
        """
        self._id = id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this EntityDiscovered.
        The `OCID`__ of the agent used for monitoring.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this EntityDiscovered.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this EntityDiscovered.
        The `OCID`__ of the agent used for monitoring.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this EntityDiscovered.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def connector_id(self):
        """
        Gets the connector_id of this EntityDiscovered.
        The `OCID`__ of the associated connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connector_id of this EntityDiscovered.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this EntityDiscovered.
        The `OCID`__ of the associated connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connector_id: The connector_id of this EntityDiscovered.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this EntityDiscovered.
        The name of the entity.


        :return: The display_name of this EntityDiscovered.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EntityDiscovered.
        The name of the entity.


        :param display_name: The display_name of this EntityDiscovered.
        :type: str
        """
        self._display_name = display_name

    @property
    def version(self):
        """
        Gets the version of this EntityDiscovered.
        The version of the entity.


        :return: The version of this EntityDiscovered.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this EntityDiscovered.
        The version of the entity.


        :param version: The version of this EntityDiscovered.
        :type: str
        """
        self._version = version

    @property
    def internal_id(self):
        """
        Gets the internal_id of this EntityDiscovered.
        The internal identifier of the entity.


        :return: The internal_id of this EntityDiscovered.
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """
        Sets the internal_id of this EntityDiscovered.
        The internal identifier of the entity.


        :param internal_id: The internal_id of this EntityDiscovered.
        :type: str
        """
        self._internal_id = internal_id

    @property
    def status(self):
        """
        Gets the status of this EntityDiscovered.
        The status of the entity.


        :return: The status of this EntityDiscovered.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this EntityDiscovered.
        The status of the entity.


        :param status: The status of this EntityDiscovered.
        :type: str
        """
        self._status = status

    @property
    def discover_status(self):
        """
        Gets the discover_status of this EntityDiscovered.
        The status of the entity discovery.

        Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING"


        :return: The discover_status of this EntityDiscovered.
        :rtype: str
        """
        return self._discover_status

    @discover_status.setter
    def discover_status(self, discover_status):
        """
        Sets the discover_status of this EntityDiscovered.
        The status of the entity discovery.


        :param discover_status: The discover_status of this EntityDiscovered.
        :type: str
        """
        allowed_values = ["PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING"]
        if not value_allowed_none_or_none_sentinel(discover_status, allowed_values):
            raise ValueError(
                "Invalid value for `discover_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._discover_status = discover_status

    @property
    def discover_error_code(self):
        """
        Gets the discover_error_code of this EntityDiscovered.
        The error code of the discovery.


        :return: The discover_error_code of this EntityDiscovered.
        :rtype: str
        """
        return self._discover_error_code

    @discover_error_code.setter
    def discover_error_code(self, discover_error_code):
        """
        Sets the discover_error_code of this EntityDiscovered.
        The error code of the discovery.


        :param discover_error_code: The discover_error_code of this EntityDiscovered.
        :type: str
        """
        self._discover_error_code = discover_error_code

    @property
    def discover_error_msg(self):
        """
        Gets the discover_error_msg of this EntityDiscovered.
        The error message of the discovery.


        :return: The discover_error_msg of this EntityDiscovered.
        :rtype: str
        """
        return self._discover_error_msg

    @discover_error_msg.setter
    def discover_error_msg(self, discover_error_msg):
        """
        Sets the discover_error_msg of this EntityDiscovered.
        The error message of the discovery.


        :param discover_error_msg: The discover_error_msg of this EntityDiscovered.
        :type: str
        """
        self._discover_error_msg = discover_error_msg

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this EntityDiscovered.
        The type of discovered entities.

        Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER"


        :return: The entity_type of this EntityDiscovered.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EntityDiscovered.
        The type of discovered entities.


        :param entity_type: The entity_type of this EntityDiscovered.
        :type: str
        """
        allowed_values = ["STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            raise ValueError(
                "Invalid value for `entity_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._entity_type = entity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
