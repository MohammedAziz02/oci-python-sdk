# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210216


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProtectedDatabaseDetails(object):
    """
    Describes the parameters required to update a protected database.
    """

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "XS"
    DATABASE_SIZE_XS = "XS"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "S"
    DATABASE_SIZE_S = "S"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "M"
    DATABASE_SIZE_M = "M"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "L"
    DATABASE_SIZE_L = "L"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "XL"
    DATABASE_SIZE_XL = "XL"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "XXL"
    DATABASE_SIZE_XXL = "XXL"

    #: A constant which can be used with the database_size property of a UpdateProtectedDatabaseDetails.
    #: This constant has a value of "AUTO"
    DATABASE_SIZE_AUTO = "AUTO"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProtectedDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateProtectedDatabaseDetails.
        :type display_name: str

        :param database_size:
            The value to assign to the database_size property of this UpdateProtectedDatabaseDetails.
            Allowed values for this property are: "XS", "S", "M", "L", "XL", "XXL", "AUTO"
        :type database_size: str

        :param database_size_in_gbs:
            The value to assign to the database_size_in_gbs property of this UpdateProtectedDatabaseDetails.
        :type database_size_in_gbs: int

        :param password:
            The value to assign to the password property of this UpdateProtectedDatabaseDetails.
        :type password: str

        :param protection_policy_id:
            The value to assign to the protection_policy_id property of this UpdateProtectedDatabaseDetails.
        :type protection_policy_id: str

        :param recovery_service_subnets:
            The value to assign to the recovery_service_subnets property of this UpdateProtectedDatabaseDetails.
        :type recovery_service_subnets: list[oci.recovery.models.RecoveryServiceSubnetInput]

        :param is_redo_logs_shipped:
            The value to assign to the is_redo_logs_shipped property of this UpdateProtectedDatabaseDetails.
        :type is_redo_logs_shipped: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateProtectedDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateProtectedDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'database_size': 'str',
            'database_size_in_gbs': 'int',
            'password': 'str',
            'protection_policy_id': 'str',
            'recovery_service_subnets': 'list[RecoveryServiceSubnetInput]',
            'is_redo_logs_shipped': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'database_size': 'databaseSize',
            'database_size_in_gbs': 'databaseSizeInGBs',
            'password': 'password',
            'protection_policy_id': 'protectionPolicyId',
            'recovery_service_subnets': 'recoveryServiceSubnets',
            'is_redo_logs_shipped': 'isRedoLogsShipped',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._database_size = None
        self._database_size_in_gbs = None
        self._password = None
        self._protection_policy_id = None
        self._recovery_service_subnets = None
        self._is_redo_logs_shipped = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateProtectedDatabaseDetails.
        The protected database name. You can change the displayName. Avoid entering confidential information.


        :return: The display_name of this UpdateProtectedDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateProtectedDatabaseDetails.
        The protected database name. You can change the displayName. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateProtectedDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def database_size(self):
        """
        Gets the database_size of this UpdateProtectedDatabaseDetails.
        The size of the database is allowed to be decreased. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

        Allowed values for this property are: "XS", "S", "M", "L", "XL", "XXL", "AUTO"


        :return: The database_size of this UpdateProtectedDatabaseDetails.
        :rtype: str
        """
        return self._database_size

    @database_size.setter
    def database_size(self, database_size):
        """
        Sets the database_size of this UpdateProtectedDatabaseDetails.
        The size of the database is allowed to be decreased. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.


        :param database_size: The database_size of this UpdateProtectedDatabaseDetails.
        :type: str
        """
        allowed_values = ["XS", "S", "M", "L", "XL", "XXL", "AUTO"]
        if not value_allowed_none_or_none_sentinel(database_size, allowed_values):
            raise ValueError(
                f"Invalid value for `database_size`, must be None or one of {allowed_values}"
            )
        self._database_size = database_size

    @property
    def database_size_in_gbs(self):
        """
        Gets the database_size_in_gbs of this UpdateProtectedDatabaseDetails.
        The size of the database, in gigabytes.


        :return: The database_size_in_gbs of this UpdateProtectedDatabaseDetails.
        :rtype: int
        """
        return self._database_size_in_gbs

    @database_size_in_gbs.setter
    def database_size_in_gbs(self, database_size_in_gbs):
        """
        Sets the database_size_in_gbs of this UpdateProtectedDatabaseDetails.
        The size of the database, in gigabytes.


        :param database_size_in_gbs: The database_size_in_gbs of this UpdateProtectedDatabaseDetails.
        :type: int
        """
        self._database_size_in_gbs = database_size_in_gbs

    @property
    def password(self):
        """
        Gets the password of this UpdateProtectedDatabaseDetails.
        Password credential which can be used to connect to Protected Database.
        It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters.
        The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing.
        Password must not be same as current passsword.


        :return: The password of this UpdateProtectedDatabaseDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateProtectedDatabaseDetails.
        Password credential which can be used to connect to Protected Database.
        It must contain at least 2 uppercase, 2 lowercase, 2 numeric and 2 special characters.
        The special characters must be underscore (_), number sign (#) or hyphen (-). The password must not contain the username \"admin\", regardless of casing.
        Password must not be same as current passsword.


        :param password: The password of this UpdateProtectedDatabaseDetails.
        :type: str
        """
        self._password = password

    @property
    def protection_policy_id(self):
        """
        Gets the protection_policy_id of this UpdateProtectedDatabaseDetails.
        The OCID of the protection policy associated with the protected database.


        :return: The protection_policy_id of this UpdateProtectedDatabaseDetails.
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        """
        Sets the protection_policy_id of this UpdateProtectedDatabaseDetails.
        The OCID of the protection policy associated with the protected database.


        :param protection_policy_id: The protection_policy_id of this UpdateProtectedDatabaseDetails.
        :type: str
        """
        self._protection_policy_id = protection_policy_id

    @property
    def recovery_service_subnets(self):
        """
        Gets the recovery_service_subnets of this UpdateProtectedDatabaseDetails.
        List of recovery service subnet resources associated with the protected database.


        :return: The recovery_service_subnets of this UpdateProtectedDatabaseDetails.
        :rtype: list[oci.recovery.models.RecoveryServiceSubnetInput]
        """
        return self._recovery_service_subnets

    @recovery_service_subnets.setter
    def recovery_service_subnets(self, recovery_service_subnets):
        """
        Sets the recovery_service_subnets of this UpdateProtectedDatabaseDetails.
        List of recovery service subnet resources associated with the protected database.


        :param recovery_service_subnets: The recovery_service_subnets of this UpdateProtectedDatabaseDetails.
        :type: list[oci.recovery.models.RecoveryServiceSubnetInput]
        """
        self._recovery_service_subnets = recovery_service_subnets

    @property
    def is_redo_logs_shipped(self):
        """
        Gets the is_redo_logs_shipped of this UpdateProtectedDatabaseDetails.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional
        configuration is needed on client side.


        :return: The is_redo_logs_shipped of this UpdateProtectedDatabaseDetails.
        :rtype: bool
        """
        return self._is_redo_logs_shipped

    @is_redo_logs_shipped.setter
    def is_redo_logs_shipped(self, is_redo_logs_shipped):
        """
        Sets the is_redo_logs_shipped of this UpdateProtectedDatabaseDetails.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional
        configuration is needed on client side.


        :param is_redo_logs_shipped: The is_redo_logs_shipped of this UpdateProtectedDatabaseDetails.
        :type: bool
        """
        self._is_redo_logs_shipped = is_redo_logs_shipped

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateProtectedDatabaseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateProtectedDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateProtectedDatabaseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateProtectedDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateProtectedDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateProtectedDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateProtectedDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateProtectedDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
