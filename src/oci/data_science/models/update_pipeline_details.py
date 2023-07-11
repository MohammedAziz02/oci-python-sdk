# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePipelineDetails(object):
    """
    The information of pipeline to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdatePipelineDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdatePipelineDetails.
        :type description: str

        :param configuration_details:
            The value to assign to the configuration_details property of this UpdatePipelineDetails.
        :type configuration_details: oci.data_science.models.PipelineConfigurationDetails

        :param log_configuration_details:
            The value to assign to the log_configuration_details property of this UpdatePipelineDetails.
        :type log_configuration_details: oci.data_science.models.PipelineLogConfigurationDetails

        :param step_details:
            The value to assign to the step_details property of this UpdatePipelineDetails.
        :type step_details: list[oci.data_science.models.PipelineStepUpdateDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePipelineDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePipelineDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'configuration_details': 'PipelineConfigurationDetails',
            'log_configuration_details': 'PipelineLogConfigurationDetails',
            'step_details': 'list[PipelineStepUpdateDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'configuration_details': 'configurationDetails',
            'log_configuration_details': 'logConfigurationDetails',
            'step_details': 'stepDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._configuration_details = None
        self._log_configuration_details = None
        self._step_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePipelineDetails.
        A user-friendly display name for the resource.


        :return: The display_name of this UpdatePipelineDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePipelineDetails.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this UpdatePipelineDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdatePipelineDetails.
        A short description for the resource.


        :return: The description of this UpdatePipelineDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdatePipelineDetails.
        A short description for the resource.


        :param description: The description of this UpdatePipelineDetails.
        :type: str
        """
        self._description = description

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this UpdatePipelineDetails.

        :return: The configuration_details of this UpdatePipelineDetails.
        :rtype: oci.data_science.models.PipelineConfigurationDetails
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this UpdatePipelineDetails.

        :param configuration_details: The configuration_details of this UpdatePipelineDetails.
        :type: oci.data_science.models.PipelineConfigurationDetails
        """
        self._configuration_details = configuration_details

    @property
    def log_configuration_details(self):
        """
        Gets the log_configuration_details of this UpdatePipelineDetails.

        :return: The log_configuration_details of this UpdatePipelineDetails.
        :rtype: oci.data_science.models.PipelineLogConfigurationDetails
        """
        return self._log_configuration_details

    @log_configuration_details.setter
    def log_configuration_details(self, log_configuration_details):
        """
        Sets the log_configuration_details of this UpdatePipelineDetails.

        :param log_configuration_details: The log_configuration_details of this UpdatePipelineDetails.
        :type: oci.data_science.models.PipelineLogConfigurationDetails
        """
        self._log_configuration_details = log_configuration_details

    @property
    def step_details(self):
        """
        Gets the step_details of this UpdatePipelineDetails.
        Array of update details for each step. Only step configurations are allowed to be updated.


        :return: The step_details of this UpdatePipelineDetails.
        :rtype: list[oci.data_science.models.PipelineStepUpdateDetails]
        """
        return self._step_details

    @step_details.setter
    def step_details(self, step_details):
        """
        Sets the step_details of this UpdatePipelineDetails.
        Array of update details for each step. Only step configurations are allowed to be updated.


        :param step_details: The step_details of this UpdatePipelineDetails.
        :type: list[oci.data_science.models.PipelineStepUpdateDetails]
        """
        self._step_details = step_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePipelineDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdatePipelineDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePipelineDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdatePipelineDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdatePipelineDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePipelineDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdatePipelineDetails.
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
