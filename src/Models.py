from typing import List
from dataclasses import dataclass, field


@dataclass
class Ticket:
    start: str
    end: str
    price: int = 0


@dataclass
class City:
    name: str
    wharf: bool = False


@dataclass
class Road:
    start: City
    end: City
    length: int = 0
    color: List[str] = field(default_factory=list)
    type: List[str] = field(default_factory=list)
