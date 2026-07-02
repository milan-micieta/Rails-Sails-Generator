from typing import List
from dataclasses import dataclass, field

@dataclass
class City:
    name: str
    wharf: bool = False

@dataclass
class Ticket:
    start: City
    end: City
    points: int = 0



@dataclass
class Road:
    start: City
    end: City
    length: int = 0
    color: List[str] = field(default_factory=list)
    type: List[str] = field(default_factory=list)
