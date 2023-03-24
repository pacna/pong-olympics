from dataclasses import dataclass, field
from typing import Generic, TypeVar

from shared.types.key_value_pair import KeyValuePair
from .bus import Bus
from interfaces.ihandler import IHandler
import entity

T = TypeVar("T")

@dataclass
class MessageBusFactory(Generic[T]):
    bus: Bus
    handlers: list[IHandler] = field(default_factory= lambda : [
        entity.score_board
    ])

    def send(self, key: str, value: T) -> None:
        self.bus.add(KeyValuePair(key = key, value= value))

    def run(self) -> None:
        if self.bus.is_empty():
            return
        
        for handler in self.handlers:
            handler.handle_msg(msg= self.bus.peek())

        self.bus.remove()