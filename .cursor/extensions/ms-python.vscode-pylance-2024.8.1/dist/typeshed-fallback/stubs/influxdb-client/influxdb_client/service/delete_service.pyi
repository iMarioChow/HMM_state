from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class DeleteService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def post_delete(self, delete_predicate_request, **kwargs): ...
    def post_delete_with_http_info(self, delete_predicate_request, **kwargs): ...
    async def post_delete_async(self, delete_predicate_request, **kwargs): ...
