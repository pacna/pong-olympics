from dataclasses import dataclass, field
from typing import Generic, Sequence, TypeVar
from shared.types.key_value_pair import KeyValuePair
from interfaces.ihandler import IHandler
from .bus import Bus
import entity

T = TypeVar("T")

@dataclass
class MessageBusFactory(Generic[T]):
    bus: Bus = field(default_factory= Bus)
    handlers: Sequence[IHandler] = field(default_factory= lambda : [
        entity.score_board
    ])

    def send(self, key: str, value: T) -> None:
        self.bus.add(KeyValuePair[str, T](key = key, value= value))

    def run(self) -> None:
        if self.bus.is_empty():
            return
        
        for handler in self.handlers:
            handler.handle_msg(msg= self.bus.peek())

        self.bus.remove()