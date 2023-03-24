from typing import Protocol

from shared.types.key_value_pair import KeyValuePair

class IHandler(Protocol):
    def handle_msg(self, msg: KeyValuePair) -> None:
        ...