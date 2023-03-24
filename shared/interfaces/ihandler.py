from typing import Generic, Protocol, TypeVar

from shared.types.key_value_pair import KeyValuePair

T = TypeVar("T")

class IHandler(Protocol, Generic[T]):
    def handle_msg(self, msg: KeyValuePair[T]) -> None:
        ...