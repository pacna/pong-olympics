from collections import deque
from dataclasses import dataclass, field
from typing import TypeVar

from shared.types.key_value_pair import KeyValuePair

T = TypeVar("T")

@dataclass
class Bus:
    queue: deque[KeyValuePair] = field(default_factory= deque[KeyValuePair])

    def add(self, msg: KeyValuePair) -> None:
        self.queue.append(msg)

    def remove(self) -> None:
        self.queue.popleft()

    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def peek(self) -> KeyValuePair:
        return self.queue[0] or None

