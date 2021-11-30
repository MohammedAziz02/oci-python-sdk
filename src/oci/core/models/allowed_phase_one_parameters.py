# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedPhaseOneParameters(object):
    """
    Phase One Parameters
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedPhaseOneParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_algorithms:
            The value to assign to the encryption_algorithms property of this AllowedPhaseOneParameters.
        :type encryption_algorithms: list[str]

        :param authentication_algorithms:
            The value to assign to the authentication_algorithms property of this AllowedPhaseOneParameters.
        :type authentication_algorithms: list[str]

        :param dh_groups:
            The value to assign to the dh_groups property of this AllowedPhaseOneParameters.
        :type dh_groups: list[str]

        """
        self.swagger_types = {
            'encryption_algorithms': 'list[str]',
            'authentication_algorithms': 'list[str]',
            'dh_groups': 'list[str]'
        }

        self.attribute_map = {
            'encryption_algorithms': 'encryptionAlgorithms',
            'authentication_algorithms': 'authenticationAlgorithms',
            'dh_groups': 'dhGroups'
        }

        self._encryption_algorithms = None
        self._authentication_algorithms = None
        self._dh_groups = None

    @property
    def encryption_algorithms(self):
        """
        Gets the encryption_algorithms of this AllowedPhaseOneParameters.
        Phase One Encryption Algorithms


        :return: The encryption_algorithms of this AllowedPhaseOneParameters.
        :rtype: list[str]
        """
        return self._encryption_algorithms

    @encryption_algorithms.setter
    def encryption_algorithms(self, encryption_algorithms):
        """
        Sets the encryption_algorithms of this AllowedPhaseOneParameters.
        Phase One Encryption Algorithms


        :param encryption_algorithms: The encryption_algorithms of this AllowedPhaseOneParameters.
        :type: list[str]
        """
        self._encryption_algorithms = encryption_algorithms

    @property
    def authentication_algorithms(self):
        """
        Gets the authentication_algorithms of this AllowedPhaseOneParameters.
        Phase One Authentication Algorithms


        :return: The authentication_algorithms of this AllowedPhaseOneParameters.
        :rtype: list[str]
        """
        return self._authentication_algorithms

    @authentication_algorithms.setter
    def authentication_algorithms(self, authentication_algorithms):
        """
        Sets the authentication_algorithms of this AllowedPhaseOneParameters.
        Phase One Authentication Algorithms


        :param authentication_algorithms: The authentication_algorithms of this AllowedPhaseOneParameters.
        :type: list[str]
        """
        self._authentication_algorithms = authentication_algorithms

    @property
    def dh_groups(self):
        """
        Gets the dh_groups of this AllowedPhaseOneParameters.
        DH Groups


        :return: The dh_groups of this AllowedPhaseOneParameters.
        :rtype: list[str]
        """
        return self._dh_groups

    @dh_groups.setter
    def dh_groups(self, dh_groups):
        """
        Sets the dh_groups of this AllowedPhaseOneParameters.
        DH Groups


        :param dh_groups: The dh_groups of this AllowedPhaseOneParameters.
        :type: list[str]
        """
        self._dh_groups = dh_groups

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
