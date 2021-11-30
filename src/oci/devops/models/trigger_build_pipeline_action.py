# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .trigger_action import TriggerAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TriggerBuildPipelineAction(TriggerAction):
    """
    The action to trigger a build pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TriggerBuildPipelineAction object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.TriggerBuildPipelineAction.type` attribute
        of this class is ``TRIGGER_BUILD_PIPELINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TriggerBuildPipelineAction.
            Allowed values for this property are: "TRIGGER_BUILD_PIPELINE"
        :type type: str

        :param filter:
            The value to assign to the filter property of this TriggerBuildPipelineAction.
        :type filter: oci.devops.models.Filter

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this TriggerBuildPipelineAction.
        :type build_pipeline_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'filter': 'Filter',
            'build_pipeline_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'filter': 'filter',
            'build_pipeline_id': 'buildPipelineId'
        }

        self._type = None
        self._filter = None
        self._build_pipeline_id = None
        self._type = 'TRIGGER_BUILD_PIPELINE'

    @property
    def build_pipeline_id(self):
        """
        **[Required]** Gets the build_pipeline_id of this TriggerBuildPipelineAction.
        The OCID of the build pipeline to be triggered.


        :return: The build_pipeline_id of this TriggerBuildPipelineAction.
        :rtype: str
        """
        return self._build_pipeline_id

    @build_pipeline_id.setter
    def build_pipeline_id(self, build_pipeline_id):
        """
        Sets the build_pipeline_id of this TriggerBuildPipelineAction.
        The OCID of the build pipeline to be triggered.


        :param build_pipeline_id: The build_pipeline_id of this TriggerBuildPipelineAction.
        :type: str
        """
        self._build_pipeline_id = build_pipeline_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
