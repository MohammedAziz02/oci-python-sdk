# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReportTaskInfo(object):
    """
    SQL Tuning advisor task general info.
    """

    #: A constant which can be used with the status property of a SqlTuningAdvisorTaskSummaryReportTaskInfo.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a SqlTuningAdvisorTaskSummaryReportTaskInfo.
    #: This constant has a value of "INITIAL"
    STATUS_INITIAL = "INITIAL"

    #: A constant which can be used with the status property of a SqlTuningAdvisorTaskSummaryReportTaskInfo.
    #: This constant has a value of "EXECUTING"
    STATUS_EXECUTING = "EXECUTING"

    #: A constant which can be used with the status property of a SqlTuningAdvisorTaskSummaryReportTaskInfo.
    #: This constant has a value of "INTERRUPTED"
    STATUS_INTERRUPTED = "INTERRUPTED"

    #: A constant which can be used with the status property of a SqlTuningAdvisorTaskSummaryReportTaskInfo.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReportTaskInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type id: int

        :param name:
            The value to assign to the name property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type name: str

        :param description:
            The value to assign to the description property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type description: str

        :param owner:
            The value to assign to the owner property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type owner: str

        :param status:
            The value to assign to the status property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
            Allowed values for this property are: "COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_started:
            The value to assign to the time_started property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type time_ended: datetime

        :param running_time:
            The value to assign to the running_time property of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type running_time: int

        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'description': 'str',
            'owner': 'str',
            'status': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'running_time': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'owner': 'owner',
            'status': 'status',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'running_time': 'runningTime'
        }

        self._id = None
        self._name = None
        self._description = None
        self._owner = None
        self._status = None
        self._time_started = None
        self._time_ended = None
        self._running_time = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task id. It is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task id. It is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task name.


        :return: The name of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task name.


        :param name: The name of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task description. Not defined on Auto SQL Tuning tasks.


        :return: The description of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task description. Not defined on Auto SQL Tuning tasks.


        :param description: The description of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task user owner.


        :return: The owner of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task user owner.


        :param owner: The owner of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: str
        """
        self._owner = owner

    @property
    def status(self):
        """
        Gets the status of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task status. Not defined on Auto SQL Tuning tasks.

        Allowed values for this property are: "COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The SQL Tuning Advisor task status. Not defined on Auto SQL Tuning tasks.


        :param status: The status of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: str
        """
        allowed_values = ["COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        Start timestamp of task execution.


        :return: The time_started of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        Start timestamp of task execution.


        :param time_started: The time_started of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        **[Required]** Gets the time_ended of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        End timestamp of task execution.


        :return: The time_ended of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        End timestamp of task execution.


        :param time_ended: The time_ended of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def running_time(self):
        """
        Gets the running_time of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The total running time in seconds. Not defined on Auto SQL Tuning tasks.


        :return: The running_time of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :rtype: int
        """
        return self._running_time

    @running_time.setter
    def running_time(self, running_time):
        """
        Sets the running_time of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        The total running time in seconds. Not defined on Auto SQL Tuning tasks.


        :param running_time: The running_time of this SqlTuningAdvisorTaskSummaryReportTaskInfo.
        :type: int
        """
        self._running_time = running_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
