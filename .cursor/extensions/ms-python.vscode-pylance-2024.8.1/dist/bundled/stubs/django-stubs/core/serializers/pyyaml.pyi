from typing import Any

from django.core.serializers.python import Serializer as PythonSerializer
from yaml import CSafeDumper as SafeDumper

class DjangoSafeDumper(SafeDumper):
    def represent_decimal(self, data: Any) -> Any: ...
    def represent_ordered_dict(self, data: Any) -> Any: ...

class Serializer(PythonSerializer):
    internal_use_only: bool = ...
    def handle_field(self, obj: Any, field: Any) -> None: ...
    def end_serialization(self) -> None: ...
    def getvalue(self) -> Any: ...

def Deserializer(stream_or_string: Any, **options: Any) -> None: ...
