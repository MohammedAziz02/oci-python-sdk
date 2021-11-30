# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildPipelineStageRunProgress(object):
    """
    The details about the run progress of a stage in a build run.
    """

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a BuildPipelineStageRunProgress.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildPipelineStageRunProgress object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.DeliverArtifactStageRunProgress`
        * :class:`~oci.devops.models.WaitStageRunProgress`
        * :class:`~oci.devops.models.TriggerDeploymentPipelineStageRunProgress`
        * :class:`~oci.devops.models.BuildStageRunProgress`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param stage_display_name:
            The value to assign to the stage_display_name property of this BuildPipelineStageRunProgress.
        :type stage_display_name: str

        :param build_pipeline_stage_type:
            The value to assign to the build_pipeline_stage_type property of this BuildPipelineStageRunProgress.
        :type build_pipeline_stage_type: str

        :param build_pipeline_stage_id:
            The value to assign to the build_pipeline_stage_id property of this BuildPipelineStageRunProgress.
        :type build_pipeline_stage_id: str

        :param time_started:
            The value to assign to the time_started property of this BuildPipelineStageRunProgress.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this BuildPipelineStageRunProgress.
        :type time_finished: datetime

        :param status:
            The value to assign to the status property of this BuildPipelineStageRunProgress.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param build_pipeline_stage_predecessors:
            The value to assign to the build_pipeline_stage_predecessors property of this BuildPipelineStageRunProgress.
        :type build_pipeline_stage_predecessors: oci.devops.models.BuildPipelineStagePredecessorCollection

        """
        self.swagger_types = {
            'stage_display_name': 'str',
            'build_pipeline_stage_type': 'str',
            'build_pipeline_stage_id': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'status': 'str',
            'build_pipeline_stage_predecessors': 'BuildPipelineStagePredecessorCollection'
        }

        self.attribute_map = {
            'stage_display_name': 'stageDisplayName',
            'build_pipeline_stage_type': 'buildPipelineStageType',
            'build_pipeline_stage_id': 'buildPipelineStageId',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'status': 'status',
            'build_pipeline_stage_predecessors': 'buildPipelineStagePredecessors'
        }

        self._stage_display_name = None
        self._build_pipeline_stage_type = None
        self._build_pipeline_stage_id = None
        self._time_started = None
        self._time_finished = None
        self._status = None
        self._build_pipeline_stage_predecessors = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['buildPipelineStageType']

        if type == 'DELIVER_ARTIFACT':
            return 'DeliverArtifactStageRunProgress'

        if type == 'WAIT':
            return 'WaitStageRunProgress'

        if type == 'TRIGGER_DEPLOYMENT_PIPELINE':
            return 'TriggerDeploymentPipelineStageRunProgress'

        if type == 'BUILD':
            return 'BuildStageRunProgress'
        else:
            return 'BuildPipelineStageRunProgress'

    @property
    def stage_display_name(self):
        """
        Gets the stage_display_name of this BuildPipelineStageRunProgress.
        Build Run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The stage_display_name of this BuildPipelineStageRunProgress.
        :rtype: str
        """
        return self._stage_display_name

    @stage_display_name.setter
    def stage_display_name(self, stage_display_name):
        """
        Sets the stage_display_name of this BuildPipelineStageRunProgress.
        Build Run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param stage_display_name: The stage_display_name of this BuildPipelineStageRunProgress.
        :type: str
        """
        self._stage_display_name = stage_display_name

    @property
    def build_pipeline_stage_type(self):
        """
        Gets the build_pipeline_stage_type of this BuildPipelineStageRunProgress.
        Stage types.


        :return: The build_pipeline_stage_type of this BuildPipelineStageRunProgress.
        :rtype: str
        """
        return self._build_pipeline_stage_type

    @build_pipeline_stage_type.setter
    def build_pipeline_stage_type(self, build_pipeline_stage_type):
        """
        Sets the build_pipeline_stage_type of this BuildPipelineStageRunProgress.
        Stage types.


        :param build_pipeline_stage_type: The build_pipeline_stage_type of this BuildPipelineStageRunProgress.
        :type: str
        """
        self._build_pipeline_stage_type = build_pipeline_stage_type

    @property
    def build_pipeline_stage_id(self):
        """
        Gets the build_pipeline_stage_id of this BuildPipelineStageRunProgress.
        The stage OCID.


        :return: The build_pipeline_stage_id of this BuildPipelineStageRunProgress.
        :rtype: str
        """
        return self._build_pipeline_stage_id

    @build_pipeline_stage_id.setter
    def build_pipeline_stage_id(self, build_pipeline_stage_id):
        """
        Sets the build_pipeline_stage_id of this BuildPipelineStageRunProgress.
        The stage OCID.


        :param build_pipeline_stage_id: The build_pipeline_stage_id of this BuildPipelineStageRunProgress.
        :type: str
        """
        self._build_pipeline_stage_id = build_pipeline_stage_id

    @property
    def time_started(self):
        """
        Gets the time_started of this BuildPipelineStageRunProgress.
        The time the stage started executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this BuildPipelineStageRunProgress.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this BuildPipelineStageRunProgress.
        The time the stage started executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this BuildPipelineStageRunProgress.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this BuildPipelineStageRunProgress.
        The time the stage finished executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this BuildPipelineStageRunProgress.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this BuildPipelineStageRunProgress.
        The time the stage finished executing. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this BuildPipelineStageRunProgress.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def status(self):
        """
        Gets the status of this BuildPipelineStageRunProgress.
        The current status of the stage.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this BuildPipelineStageRunProgress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildPipelineStageRunProgress.
        The current status of the stage.


        :param status: The status of this BuildPipelineStageRunProgress.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def build_pipeline_stage_predecessors(self):
        """
        Gets the build_pipeline_stage_predecessors of this BuildPipelineStageRunProgress.

        :return: The build_pipeline_stage_predecessors of this BuildPipelineStageRunProgress.
        :rtype: oci.devops.models.BuildPipelineStagePredecessorCollection
        """
        return self._build_pipeline_stage_predecessors

    @build_pipeline_stage_predecessors.setter
    def build_pipeline_stage_predecessors(self, build_pipeline_stage_predecessors):
        """
        Sets the build_pipeline_stage_predecessors of this BuildPipelineStageRunProgress.

        :param build_pipeline_stage_predecessors: The build_pipeline_stage_predecessors of this BuildPipelineStageRunProgress.
        :type: oci.devops.models.BuildPipelineStagePredecessorCollection
        """
        self._build_pipeline_stage_predecessors = build_pipeline_stage_predecessors

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
