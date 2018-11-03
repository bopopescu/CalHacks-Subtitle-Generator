"""Generated client library for accesscontextmanager version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.accesscontextmanager.v1alpha import accesscontextmanager_v1alpha_messages as messages


class AccesscontextmanagerV1alpha(base_api.BaseApiClient):
  """Generated client library for service accesscontextmanager version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://accesscontextmanager.googleapis.com/'

  _PACKAGE = u'accesscontextmanager'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'AccesscontextmanagerV1alpha'
  _URL_VERSION = u'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new accesscontextmanager handle."""
    url = url or self.BASE_URL
    super(AccesscontextmanagerV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.accessPolicies_accessLevels = self.AccessPoliciesAccessLevelsService(self)
    self.accessPolicies_accessZones = self.AccessPoliciesAccessZonesService(self)
    self.accessPolicies = self.AccessPoliciesService(self)
    self.operations = self.OperationsService(self)

  class AccessPoliciesAccessLevelsService(base_api.BaseApiService):
    """Service class for the accessPolicies_accessLevels resource."""

    _NAME = u'accessPolicies_accessLevels'

    def __init__(self, client):
      super(AccesscontextmanagerV1alpha.AccessPoliciesAccessLevelsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an Access Level. The longrunning.
operation from this RPC will have a successful status once the Access
Level has
propagated to long-lasting storage. Access Levels containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessLevels',
        http_method=u'POST',
        method_id=u'accesscontextmanager.accessPolicies.accessLevels.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/accessLevels',
        request_field=u'accessLevel',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an Access Level by resource.
name. The longrunning operation from this RPC will have a successful status
once the Access Level has been removed
from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method=u'DELETE',
        method_id=u'accesscontextmanager.accessPolicies.accessLevels.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an Access Level by resource.
name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessLevel) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.accessLevels.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'accessLevelFormat'],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest',
        response_type_name=u'AccessLevel',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all Access Levels for an access.
policy.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAccessLevelsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessLevels',
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.accessLevels.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'accessLevelFormat', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+parent}/accessLevels',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessLevelsListRequest',
        response_type_name=u'ListAccessLevelsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an Access Level. The longrunning.
operation from this RPC will have a successful status once the changes to
the Access Level have propagated
to long-lasting storage. Access Levels containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method=u'PATCH',
        method_id=u'accesscontextmanager.accessPolicies.accessLevels.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha/{+name}',
        request_field=u'accessLevel',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class AccessPoliciesAccessZonesService(base_api.BaseApiService):
    """Service class for the accessPolicies_accessZones resource."""

    _NAME = u'accessPolicies_accessZones'

    def __init__(self, client):
      super(AccesscontextmanagerV1alpha.AccessPoliciesAccessZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an Access Zone. The longrunning.
operation from this RPC will have a successful status once the Access
Zone has
propagated to long-lasting storage. Access Zones containing errors
will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessZonesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessZones',
        http_method=u'POST',
        method_id=u'accesscontextmanager.accessPolicies.accessZones.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha/{+parent}/accessZones',
        request_field=u'accessZone',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessZonesCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an Access Zone by resource name.
The longrunning operation from this RPC will have a successful status once
the Access Zone
has been removed from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessZonesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessZones/{accessZonesId}',
        http_method=u'DELETE',
        method_id=u'accesscontextmanager.accessPolicies.accessZones.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessZonesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an Access Zone by resource name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessZonesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessZone) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessZones/{accessZonesId}',
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.accessZones.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessZonesGetRequest',
        response_type_name=u'AccessZone',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all Access Zones for an access.
policy.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessZonesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAccessZonesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessZones',
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.accessZones.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha/{+parent}/accessZones',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessZonesListRequest',
        response_type_name=u'ListAccessZonesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an Access Zone. The longrunning.
operation from this RPC will have a successful status once the changes to
the Access Zone
have propagated to long-lasting storage. Access Zone containing errors
will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessZonesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}/accessZones/{accessZonesId}',
        http_method=u'PATCH',
        method_id=u'accesscontextmanager.accessPolicies.accessZones.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha/{+name}',
        request_field=u'accessZone',
        request_type_name=u'AccesscontextmanagerAccessPoliciesAccessZonesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class AccessPoliciesService(base_api.BaseApiService):
    """Service class for the accessPolicies resource."""

    _NAME = u'accessPolicies'

    def __init__(self, client):
      super(AccesscontextmanagerV1alpha.AccessPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an `AccessPolicy`. Fails if this organization already has a.
`AccessPolicy`. The longrunning Operation will have a successful status
once the `AccessPolicy` has propagated to long-lasting storage.
Syntactic and basic semantic errors will be returned in `metadata` as a
BadRequest proto.

      Args:
        request: (AccessPolicy) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'accesscontextmanager.accessPolicies.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1alpha/accessPolicies',
        request_field='<request>',
        request_type_name=u'AccessPolicy',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an AccessPolicy by resource.
name. The longrunning Operation will have a successful status once the
AccessPolicy
has been removed from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}',
        http_method=u'DELETE',
        method_id=u'accesscontextmanager.accessPolicies.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an AccessPolicy by name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}',
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesGetRequest',
        response_type_name=u'AccessPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all AccessPolicies under a.
container.

      Args:
        request: (AccesscontextmanagerAccessPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAccessPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'accesscontextmanager.accessPolicies.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'pageSize', u'pageToken', u'parent'],
        relative_path=u'v1alpha/accessPolicies',
        request_field='',
        request_type_name=u'AccesscontextmanagerAccessPoliciesListRequest',
        response_type_name=u'ListAccessPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an AccessPolicy. The.
longrunning Operation from this RPC will have a successful status once the
changes to the AccessPolicy have propagated
to long-lasting storage. Syntactic and basic semantic errors will be
returned in `metadata` as a BadRequest proto.

      Args:
        request: (AccesscontextmanagerAccessPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/accessPolicies/{accessPoliciesId}',
        http_method=u'PATCH',
        method_id=u'accesscontextmanager.accessPolicies.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha/{+name}',
        request_field=u'accessPolicy',
        request_type_name=u'AccesscontextmanagerAccessPoliciesPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(AccesscontextmanagerV1alpha.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AccesscontextmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'accesscontextmanager.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha/{+name}',
        request_field='',
        request_type_name=u'AccesscontextmanagerOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )
