# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelDetails(object):
    """
    Parameters needed to create a new model. Models are mathematical representations of the relationships between data. Models are represented by their associated metadata and artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateModelDetails.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this CreateModelDetails.
        :type project_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateModelDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateModelDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateModelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateModelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param custom_metadata_list:
            The value to assign to the custom_metadata_list property of this CreateModelDetails.
        :type custom_metadata_list: list[oci.data_science.models.Metadata]

        :param defined_metadata_list:
            The value to assign to the defined_metadata_list property of this CreateModelDetails.
        :type defined_metadata_list: list[oci.data_science.models.Metadata]

        :param input_schema:
            The value to assign to the input_schema property of this CreateModelDetails.
        :type input_schema: str

        :param output_schema:
            The value to assign to the output_schema property of this CreateModelDetails.
        :type output_schema: str

        :param model_version_set_id:
            The value to assign to the model_version_set_id property of this CreateModelDetails.
        :type model_version_set_id: str

        :param version_label:
            The value to assign to the version_label property of this CreateModelDetails.
        :type version_label: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'project_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'custom_metadata_list': 'list[Metadata]',
            'defined_metadata_list': 'list[Metadata]',
            'input_schema': 'str',
            'output_schema': 'str',
            'model_version_set_id': 'str',
            'version_label': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'custom_metadata_list': 'customMetadataList',
            'defined_metadata_list': 'definedMetadataList',
            'input_schema': 'inputSchema',
            'output_schema': 'outputSchema',
            'model_version_set_id': 'modelVersionSetId',
            'version_label': 'versionLabel'
        }

        self._compartment_id = None
        self._project_id = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._custom_metadata_list = None
        self._defined_metadata_list = None
        self._input_schema = None
        self._output_schema = None
        self._model_version_set_id = None
        self._version_label = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateModelDetails.
        The `OCID`__ of the compartment to create the model in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateModelDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateModelDetails.
        The `OCID`__ of the compartment to create the model in.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateModelDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateModelDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateModelDetails.
        The `OCID`__ of the project to associate with the model.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateModelDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My Model`


        :return: The display_name of this CreateModelDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateModelDetails.
        A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.
        Example: `My Model`


        :param display_name: The display_name of this CreateModelDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateModelDetails.
        A short description of the model.


        :return: The description of this CreateModelDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateModelDetails.
        A short description of the model.


        :param description: The description of this CreateModelDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateModelDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateModelDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateModelDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateModelDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateModelDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateModelDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def custom_metadata_list(self):
        """
        Gets the custom_metadata_list of this CreateModelDetails.
        An array of custom metadata details for the model.


        :return: The custom_metadata_list of this CreateModelDetails.
        :rtype: list[oci.data_science.models.Metadata]
        """
        return self._custom_metadata_list

    @custom_metadata_list.setter
    def custom_metadata_list(self, custom_metadata_list):
        """
        Sets the custom_metadata_list of this CreateModelDetails.
        An array of custom metadata details for the model.


        :param custom_metadata_list: The custom_metadata_list of this CreateModelDetails.
        :type: list[oci.data_science.models.Metadata]
        """
        self._custom_metadata_list = custom_metadata_list

    @property
    def defined_metadata_list(self):
        """
        Gets the defined_metadata_list of this CreateModelDetails.
        An array of defined metadata details for the model.


        :return: The defined_metadata_list of this CreateModelDetails.
        :rtype: list[oci.data_science.models.Metadata]
        """
        return self._defined_metadata_list

    @defined_metadata_list.setter
    def defined_metadata_list(self, defined_metadata_list):
        """
        Sets the defined_metadata_list of this CreateModelDetails.
        An array of defined metadata details for the model.


        :param defined_metadata_list: The defined_metadata_list of this CreateModelDetails.
        :type: list[oci.data_science.models.Metadata]
        """
        self._defined_metadata_list = defined_metadata_list

    @property
    def input_schema(self):
        """
        Gets the input_schema of this CreateModelDetails.
        Input schema file content in String format


        :return: The input_schema of this CreateModelDetails.
        :rtype: str
        """
        return self._input_schema

    @input_schema.setter
    def input_schema(self, input_schema):
        """
        Sets the input_schema of this CreateModelDetails.
        Input schema file content in String format


        :param input_schema: The input_schema of this CreateModelDetails.
        :type: str
        """
        self._input_schema = input_schema

    @property
    def output_schema(self):
        """
        Gets the output_schema of this CreateModelDetails.
        Output schema file content in String format


        :return: The output_schema of this CreateModelDetails.
        :rtype: str
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema):
        """
        Sets the output_schema of this CreateModelDetails.
        Output schema file content in String format


        :param output_schema: The output_schema of this CreateModelDetails.
        :type: str
        """
        self._output_schema = output_schema

    @property
    def model_version_set_id(self):
        """
        Gets the model_version_set_id of this CreateModelDetails.
        The OCID of the model version set that the model is associated to.


        :return: The model_version_set_id of this CreateModelDetails.
        :rtype: str
        """
        return self._model_version_set_id

    @model_version_set_id.setter
    def model_version_set_id(self, model_version_set_id):
        """
        Sets the model_version_set_id of this CreateModelDetails.
        The OCID of the model version set that the model is associated to.


        :param model_version_set_id: The model_version_set_id of this CreateModelDetails.
        :type: str
        """
        self._model_version_set_id = model_version_set_id

    @property
    def version_label(self):
        """
        Gets the version_label of this CreateModelDetails.
        The version label can add an additional description of the lifecycle state of the model or the application using/training the model.


        :return: The version_label of this CreateModelDetails.
        :rtype: str
        """
        return self._version_label

    @version_label.setter
    def version_label(self, version_label):
        """
        Sets the version_label of this CreateModelDetails.
        The version label can add an additional description of the lifecycle state of the model or the application using/training the model.


        :param version_label: The version_label of this CreateModelDetails.
        :type: str
        """
        self._version_label = version_label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
