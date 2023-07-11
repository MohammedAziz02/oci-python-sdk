# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadBalancerConfig(object):
    """
    Specifies configuration for load balancer traffic shift stages.
    The load balancer specified here should be an Application load balancer type.
    Network load balancers are not supported.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoadBalancerConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this LoadBalancerConfig.
        :type load_balancer_id: str

        :param listener_name:
            The value to assign to the listener_name property of this LoadBalancerConfig.
        :type listener_name: str

        :param backend_port:
            The value to assign to the backend_port property of this LoadBalancerConfig.
        :type backend_port: int

        """
        self.swagger_types = {
            'load_balancer_id': 'str',
            'listener_name': 'str',
            'backend_port': 'int'
        }

        self.attribute_map = {
            'load_balancer_id': 'loadBalancerId',
            'listener_name': 'listenerName',
            'backend_port': 'backendPort'
        }

        self._load_balancer_id = None
        self._listener_name = None
        self._backend_port = None

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this LoadBalancerConfig.
        The OCID of the load balancer.


        :return: The load_balancer_id of this LoadBalancerConfig.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this LoadBalancerConfig.
        The OCID of the load balancer.


        :param load_balancer_id: The load_balancer_id of this LoadBalancerConfig.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def listener_name(self):
        """
        **[Required]** Gets the listener_name of this LoadBalancerConfig.
        Name of the load balancer listener.


        :return: The listener_name of this LoadBalancerConfig.
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        """
        Sets the listener_name of this LoadBalancerConfig.
        Name of the load balancer listener.


        :param listener_name: The listener_name of this LoadBalancerConfig.
        :type: str
        """
        self._listener_name = listener_name

    @property
    def backend_port(self):
        """
        Gets the backend_port of this LoadBalancerConfig.
        Listen port for the backend server.


        :return: The backend_port of this LoadBalancerConfig.
        :rtype: int
        """
        return self._backend_port

    @backend_port.setter
    def backend_port(self, backend_port):
        """
        Sets the backend_port of this LoadBalancerConfig.
        Listen port for the backend server.


        :param backend_port: The backend_port of this LoadBalancerConfig.
        :type: int
        """
        self._backend_port = backend_port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
