# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_vbs_instance_compartment_details import ChangeVbsInstanceCompartmentDetails
from .create_vbs_instance_details import CreateVbsInstanceDetails
from .update_vbs_instance_details import UpdateVbsInstanceDetails
from .vbs_instance import VbsInstance
from .vbs_instance_summary import VbsInstanceSummary
from .vbs_instance_summary_collection import VbsInstanceSummaryCollection
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for vbs_inst services.
vbs_inst_type_mapping = {
    "ChangeVbsInstanceCompartmentDetails": ChangeVbsInstanceCompartmentDetails,
    "CreateVbsInstanceDetails": CreateVbsInstanceDetails,
    "UpdateVbsInstanceDetails": UpdateVbsInstanceDetails,
    "VbsInstance": VbsInstance,
    "VbsInstanceSummary": VbsInstanceSummary,
    "VbsInstanceSummaryCollection": VbsInstanceSummaryCollection,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
