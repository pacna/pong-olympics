from dataclasses import dataclass, field
from .bus import Bus
from shared.interfaces.ihandler import IHandler
import entity

@dataclass
class HandlerFactory:
    bus: Bus
    handlers: list[IHandler] = field(default_factory= lambda : [
            entity.score_board
        ])

    def run(self) -> None:
        if self.bus.is_empty():
            return
        
        for handler in self.handlers:
            handler.handle_msg(msg= self.bus.peek())

        self.bus.remove()