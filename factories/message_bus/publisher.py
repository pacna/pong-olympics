from dataclasses import dataclass
from typing import Generic, TypeVar

from shared.types.key_value_pair import KeyValuePair

from .bus import Bus

T = TypeVar("T")

@dataclass
class Publisher(Generic[T]):
    bus: Bus

    def send(self, key: str, value: T) -> None:
        self.bus.add(KeyValuePair(key = key, value= value))