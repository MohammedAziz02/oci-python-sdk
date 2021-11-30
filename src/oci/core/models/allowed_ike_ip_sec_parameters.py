# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedIkeIPSecParameters(object):
    """
    Allowed IKE IPSec Parameters
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedIkeIPSecParameters object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param allowed_phase_one_parameters:
            The value to assign to the allowed_phase_one_parameters property of this AllowedIkeIPSecParameters.
        :type allowed_phase_one_parameters: oci.core.models.AllowedPhaseOneParameters

        :param allowed_phase_two_parameters:
            The value to assign to the allowed_phase_two_parameters property of this AllowedIkeIPSecParameters.
        :type allowed_phase_two_parameters: oci.core.models.AllowedPhaseTwoParameters

        :param default_phase_one_parameters:
            The value to assign to the default_phase_one_parameters property of this AllowedIkeIPSecParameters.
        :type default_phase_one_parameters: oci.core.models.DefaultPhaseOneParameters

        :param default_phase_two_parameters:
            The value to assign to the default_phase_two_parameters property of this AllowedIkeIPSecParameters.
        :type default_phase_two_parameters: oci.core.models.DefaultPhaseTwoParameters

        """
        self.swagger_types = {
            'allowed_phase_one_parameters': 'AllowedPhaseOneParameters',
            'allowed_phase_two_parameters': 'AllowedPhaseTwoParameters',
            'default_phase_one_parameters': 'DefaultPhaseOneParameters',
            'default_phase_two_parameters': 'DefaultPhaseTwoParameters'
        }

        self.attribute_map = {
            'allowed_phase_one_parameters': 'allowedPhaseOneParameters',
            'allowed_phase_two_parameters': 'allowedPhaseTwoParameters',
            'default_phase_one_parameters': 'defaultPhaseOneParameters',
            'default_phase_two_parameters': 'defaultPhaseTwoParameters'
        }

        self._allowed_phase_one_parameters = None
        self._allowed_phase_two_parameters = None
        self._default_phase_one_parameters = None
        self._default_phase_two_parameters = None

    @property
    def allowed_phase_one_parameters(self):
        """
        **[Required]** Gets the allowed_phase_one_parameters of this AllowedIkeIPSecParameters.

        :return: The allowed_phase_one_parameters of this AllowedIkeIPSecParameters.
        :rtype: oci.core.models.AllowedPhaseOneParameters
        """
        return self._allowed_phase_one_parameters

    @allowed_phase_one_parameters.setter
    def allowed_phase_one_parameters(self, allowed_phase_one_parameters):
        """
        Sets the allowed_phase_one_parameters of this AllowedIkeIPSecParameters.

        :param allowed_phase_one_parameters: The allowed_phase_one_parameters of this AllowedIkeIPSecParameters.
        :type: oci.core.models.AllowedPhaseOneParameters
        """
        self._allowed_phase_one_parameters = allowed_phase_one_parameters

    @property
    def allowed_phase_two_parameters(self):
        """
        **[Required]** Gets the allowed_phase_two_parameters of this AllowedIkeIPSecParameters.

        :return: The allowed_phase_two_parameters of this AllowedIkeIPSecParameters.
        :rtype: oci.core.models.AllowedPhaseTwoParameters
        """
        return self._allowed_phase_two_parameters

    @allowed_phase_two_parameters.setter
    def allowed_phase_two_parameters(self, allowed_phase_two_parameters):
        """
        Sets the allowed_phase_two_parameters of this AllowedIkeIPSecParameters.

        :param allowed_phase_two_parameters: The allowed_phase_two_parameters of this AllowedIkeIPSecParameters.
        :type: oci.core.models.AllowedPhaseTwoParameters
        """
        self._allowed_phase_two_parameters = allowed_phase_two_parameters

    @property
    def default_phase_one_parameters(self):
        """
        **[Required]** Gets the default_phase_one_parameters of this AllowedIkeIPSecParameters.

        :return: The default_phase_one_parameters of this AllowedIkeIPSecParameters.
        :rtype: oci.core.models.DefaultPhaseOneParameters
        """
        return self._default_phase_one_parameters

    @default_phase_one_parameters.setter
    def default_phase_one_parameters(self, default_phase_one_parameters):
        """
        Sets the default_phase_one_parameters of this AllowedIkeIPSecParameters.

        :param default_phase_one_parameters: The default_phase_one_parameters of this AllowedIkeIPSecParameters.
        :type: oci.core.models.DefaultPhaseOneParameters
        """
        self._default_phase_one_parameters = default_phase_one_parameters

    @property
    def default_phase_two_parameters(self):
        """
        **[Required]** Gets the default_phase_two_parameters of this AllowedIkeIPSecParameters.

        :return: The default_phase_two_parameters of this AllowedIkeIPSecParameters.
        :rtype: oci.core.models.DefaultPhaseTwoParameters
        """
        return self._default_phase_two_parameters

    @default_phase_two_parameters.setter
    def default_phase_two_parameters(self, default_phase_two_parameters):
        """
        Sets the default_phase_two_parameters of this AllowedIkeIPSecParameters.

        :param default_phase_two_parameters: The default_phase_two_parameters of this AllowedIkeIPSecParameters.
        :type: oci.core.models.DefaultPhaseTwoParameters
        """
        self._default_phase_two_parameters = default_phase_two_parameters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
