# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221109


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchModelOperation(object):
    """
    The metadata which can be edited after model creation.
    """

    #: A constant which can be used with the operation property of a PatchModelOperation.
    #: This constant has a value of "DELETE"
    OPERATION_DELETE = "DELETE"

    #: A constant which can be used with the operation property of a PatchModelOperation.
    #: This constant has a value of "ADD"
    OPERATION_ADD = "ADD"

    #: A constant which can be used with the operation property of a PatchModelOperation.
    #: This constant has a value of "REPLACE"
    OPERATION_REPLACE = "REPLACE"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchModelOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param path:
            The value to assign to the path property of this PatchModelOperation.
        :type path: str

        :param value:
            The value to assign to the value property of this PatchModelOperation.
        :type value: str

        :param operation:
            The value to assign to the operation property of this PatchModelOperation.
            Allowed values for this property are: "DELETE", "ADD", "REPLACE"
        :type operation: str

        """
        self.swagger_types = {
            'path': 'str',
            'value': 'str',
            'operation': 'str'
        }

        self.attribute_map = {
            'path': 'path',
            'value': 'value',
            'operation': 'operation'
        }

        self._path = None
        self._value = None
        self._operation = None

    @property
    def path(self):
        """
        Gets the path of this PatchModelOperation.
        The parameter of the resource to be changed.


        :return: The path of this PatchModelOperation.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this PatchModelOperation.
        The parameter of the resource to be changed.


        :param path: The path of this PatchModelOperation.
        :type: str
        """
        self._path = path

    @property
    def value(self):
        """
        Gets the value of this PatchModelOperation.
        The value of the parameter to be updated.


        :return: The value of this PatchModelOperation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchModelOperation.
        The value of the parameter to be updated.


        :param value: The value of this PatchModelOperation.
        :type: str
        """
        self._value = value

    @property
    def operation(self):
        """
        Gets the operation of this PatchModelOperation.
        The value of the parameter to be updated.

        Allowed values for this property are: "DELETE", "ADD", "REPLACE"


        :return: The operation of this PatchModelOperation.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this PatchModelOperation.
        The value of the parameter to be updated.


        :param operation: The operation of this PatchModelOperation.
        :type: str
        """
        allowed_values = ["DELETE", "ADD", "REPLACE"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            raise ValueError(
                f"Invalid value for `operation`, must be None or one of {allowed_values}"
            )
        self._operation = operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
