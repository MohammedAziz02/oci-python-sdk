# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .deploy_stage_summary import DeployStageSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShellDeployStageSummary(DeployStageSummary):
    """
    Specifies the shell stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShellDeployStageSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.ShellDeployStageSummary.deploy_stage_type` attribute
        of this class is ``SHELL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ShellDeployStageSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this ShellDeployStageSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this ShellDeployStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this ShellDeployStageSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this ShellDeployStageSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ShellDeployStageSummary.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this ShellDeployStageSummary.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this ShellDeployStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ShellDeployStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ShellDeployStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ShellDeployStageSummary.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this ShellDeployStageSummary.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ShellDeployStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ShellDeployStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ShellDeployStageSummary.
        :type system_tags: dict(str, dict(str, object))

        :param container_config:
            The value to assign to the container_config property of this ShellDeployStageSummary.
        :type container_config: oci.devops.models.ContainerConfig

        :param command_spec_deploy_artifact_id:
            The value to assign to the command_spec_deploy_artifact_id property of this ShellDeployStageSummary.
        :type command_spec_deploy_artifact_id: str

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this ShellDeployStageSummary.
        :type timeout_in_seconds: int

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'container_config': 'ContainerConfig',
            'command_spec_deploy_artifact_id': 'str',
            'timeout_in_seconds': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'container_config': 'containerConfig',
            'command_spec_deploy_artifact_id': 'commandSpecDeployArtifactId',
            'timeout_in_seconds': 'timeoutInSeconds'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._container_config = None
        self._command_spec_deploy_artifact_id = None
        self._timeout_in_seconds = None
        self._deploy_stage_type = 'SHELL'

    @property
    def container_config(self):
        """
        **[Required]** Gets the container_config of this ShellDeployStageSummary.

        :return: The container_config of this ShellDeployStageSummary.
        :rtype: oci.devops.models.ContainerConfig
        """
        return self._container_config

    @container_config.setter
    def container_config(self, container_config):
        """
        Sets the container_config of this ShellDeployStageSummary.

        :param container_config: The container_config of this ShellDeployStageSummary.
        :type: oci.devops.models.ContainerConfig
        """
        self._container_config = container_config

    @property
    def command_spec_deploy_artifact_id(self):
        """
        **[Required]** Gets the command_spec_deploy_artifact_id of this ShellDeployStageSummary.
        The OCID of the artifact that contains the command specification.


        :return: The command_spec_deploy_artifact_id of this ShellDeployStageSummary.
        :rtype: str
        """
        return self._command_spec_deploy_artifact_id

    @command_spec_deploy_artifact_id.setter
    def command_spec_deploy_artifact_id(self, command_spec_deploy_artifact_id):
        """
        Sets the command_spec_deploy_artifact_id of this ShellDeployStageSummary.
        The OCID of the artifact that contains the command specification.


        :param command_spec_deploy_artifact_id: The command_spec_deploy_artifact_id of this ShellDeployStageSummary.
        :type: str
        """
        self._command_spec_deploy_artifact_id = command_spec_deploy_artifact_id

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this ShellDeployStageSummary.
        Time to wait for execution of a shell stage. Defaults to 36000 seconds.


        :return: The timeout_in_seconds of this ShellDeployStageSummary.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this ShellDeployStageSummary.
        Time to wait for execution of a shell stage. Defaults to 36000 seconds.


        :param timeout_in_seconds: The timeout_in_seconds of this ShellDeployStageSummary.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
