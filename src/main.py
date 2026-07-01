from dataclasses import dataclass, field
import networkx as nx
from typing import List, Tuple, Set, Optional

@dataclass
class Ticket:
    start: str
    end: str
    price: int = 0

@dataclass
class Road:
    start: str
    end: str
    length: int = 0
    color: List[str] = field(default_factory=list)
    type: List[str] = field(default_factory=list)


def build_graph(roads: List[Road]) -> nx.MultiGraph:
    G = nx.MultiGraph()
    for r in roads:
        for c in r.color:
            G.add_edge(r.start, r.end, weight=r.length, color=c, type=r.type)
    return G






if __name__ == "__main__":
    roads = [
        Road("Vancouver", "Anchorage", 2, ["gray"], ["hard terrain railway"]),
        Road("Vancouver", "Winnipeg", 2, ["yellow"], ["railway"]),
        Road("Vancouver", "Los Angeles", 1, ["red", "green"], ["railway"]),
        Road("Vancouver", "Tokyo", 6, ["white"], ["sea route"]),
        Road("Cambridge Bay", "Reykjavik", 6, ["white"], ["sea route"]),
        Road("Cambridge Bay", "Anchorage", 6, ["black"], ["sea route"]),
        Road("Winnipeg", "Cambridge Bay", 4, ["black"], ["railway"]),
        Road("Winnipeg", "New York", 2, ["green"], ["railway"]),
        Road("Winnipeg", "Los Angeles", 3, ["gray"], ["railway"]),
        Road("Los Angeles", "New York", 4, ["purple", "black"], ["railway"]),
        Road("Los Angeles", "Mexico", 2, ["yellow", "white"], ["railway"]),
        Road("Los Angeles", "Tokyo", 7, ["black", "green"], ["sea road"]),
        Road("Los Angeles", "Honolulu", 3, ["yellow"], ["sea road"]),
        Road("New York", "Miami", 2, ["white"], ["railway"]),
        Road("New York", "Reykjavik", 6, ["yellow"], ["sea route"]),
        Road("New York", "Edinburgh", 7, ["red", "purple"], ["sea route"]),
        Road("Miami", "Caracas", 2, ["white"], ["sea route"]),
        Road("Miami", "Casablanca", 7, ["green"], ["sea route"]),
        Road("Mexico", "Caracas", 3, ["red", "purple"], ["railway"]),
        Road("Caracas", "Lima", 2, ["white", "yellow"], ["railway"]),
        Road("Caracas", "Lagos", 7, ["red"], ["sea route"]),
        Road("Caracas", "Rio de Janeiro", 4, ["green", "black"], ["railway"]),
        Road("Lima", "Valparaiso", 2, ["grey", "grey"], ["railway"]),
        Road("Lima", "Honolulu", 6, ["grey"], ["sea route"]),
        Road("Lima", "Sydney", 8, ["black", "purple"], ["sea route"]),
        Road("Valparaiso", "Buenos Aires", 3, ["green"], ["sea route"]),
        Road("Valparaiso", "Christchurch", 7, ["yellow"], ["sea route"]),
        Road("Rio de Janeiro", "Buenos Aires", 1, ["white", "red"], ["railway"]),
        Road("Rio de Janeiro", "Cape Town", 6, ["white", "black"], ["sea route"]),
        Road("Rio de Janeiro", "Luanda", 6, ["grey"], ["sea route"]),
        Road("Buenos Aires", "Cape Town", 7, ["purple", "yellow"], ["sea route"]),
        Road("Reykjavik", "Edinburgh", 2, ["grey"], ["sea route"]),
        Road("Reykjavik", "Murmansk", 4, ["green"], ["sea route"]),
        Road("Murmansk", "Moskva", 2, ["purple"], ["railway"]),
        Road("Murmansk", "Tiksi", 7, ["red"], ["sea route"]),
        Road("Moskva", "Novosibirsk", 4, ["green", "yellow"], ["railway"]),
        Road("Moskva", "Tehran", 3, ["red"], ["railway"]),
        Road("Hamburg", "Moskva", 2, ["white", "black"], ["railway"]),
        Road("Hamburg", "Edinburgh", 1, ["yellow", "black"], ["sea route"]),
        Road("Hamburg", "Marseille", 1, ["red", "purple"], ["railway"]),
        Road("Hamburg", "Athina", 2, ["grey"], ["railway"]),
        Road("Edinburgh", "Marseille", 1, ["white", "green"], ["sea route"]),
        Road("Marseille", "Athina", 2, ["red"], ["sea route"]),
        Road("Marseille", "Casablanca", 1, ["grey"], ["hard terrain railway"]),
        Road("Athina", "Tehran", 2, ["grey"], ["railway"]),
        Road("Athina", "Al-Qahira", 1, ["green"], ["sea route"]),
        Road("Casablanca", "Al-Qahira", 3, ["grey"], ["railway"]),
        Road("Casablanca", "Lagos", 4, ["grey"], ["railway"]),
        Road("Al-Qahira", "Tehran", 1, ["yellow", "black"], ["railway"]),
        Road("Al-Qahira", "Djibouti", 2, ["red", "white"], ["railway"]),
        Road("Lagos", "Luanda", 1, ["purple", "yellow"], ["railway"]),
        Road("Djibouti", "Dar El Salaam", 1, ["red", "black"], ["railway"]),
        Road("Luanda", "Dar El Salaam", 2, ["grey"], ["hard terrain railway"]),
        Road("Luanda", "Cape Town", 2, ["grey"], ["railway"]),
        Road("Dar El Salaam", "Cape Town", 3, ["green", "purple"], ["railway"]),
        Road("Dar El Salaam", "Jakarta", 7, ["green", "purple"], ["sea route"]),
        Road("Dar El Salaam", "Mumbai", 4, ["white"], ["sea route"]),
        Road("Dar El Salaam", "Toamasina", 1, ["yellow"], ["sea route"]),
        Road("Cape Town", "Toamasina", 3, ["grey"], ["sea route"]),
        Road("Cape Town", "Empty Point", 5, ["red", "green"], ["sea route"]),
        Road("Empty Point", "Perth", 5, ["white","purple"], ["sea route"]),
        Road("Tiksi", "Novosibirsk", 3, ["grey"], ["railway"]),
        Road("Tiksi", "Yakutsk", 1, ["green"], ["railway"]),
        Road("Tiksi", "Petropavlovsk", 7, ["black"], ["sea route"]),
        Road("Tiksi", "Anchorage", 8, ["yellow"], ["sea route"]),
        Road("Novosibirsk", "Yakutsk", 3, ["purple"], ["railway"]),
        Road("Novosibirsk", "Beijing", 3, ["red", "black"], ["railway"]),
        Road("Novosibirsk", "Labore", 2, ["white"], ["railway"]),
        Road("Tehran", "Labore", 2, ["grey"], ["hard terrain railway"]),
        Road("Tehran", "Mumbai", 3, ["white", "purple"], ["railway"]),
        Road("Labore", "Beijing", 3, ["grey"], ["hard terrain railway"]),
        Road("Labore", "Mumbai", 1, ["green", "black"], ["railway"]),
        Road("Mumbai", "Bangkok", 3, ["red", "yellow"], ["railway"]),
        Road("Yakutsk", "Beijing", 3, ["yellow"], ["railway"]),
        Road("Yakutsk", "Petropavlovsk", 3, ["white"], ["railway"]),
        Road("Petropavlovsk", "Tokyo", 2, ["grey"], ["sea route"]),
        Road("Petropavlovsk", "Anchorage", 3, ["purple"], ["sea route"]),
        Road("Beijing", "Honk Kong", 2, ["white", "green"], ["railway"]),
        Road("Tokyo", "Honk Kong", 3, ["grey"], ["sea route"]),
        Road("Tokyo", "Honolulu", 5, ["red"], ["sea route"]),
        Road("Tokyo", "Manila", 2, ["yellow"], ["sea route"]),
        Road("Honk Kong", "Bangkok", 2, ["white"], ["sea route"]),
        Road("Honk Kong", "Manila", 1, ["purple"], ["sea route"]),
        Road("Honolulu", "Manila", 5, ["white"], ["sea route"]),
        Road("Honolulu", "Port Moresby", 3, ["green"], ["sea route"]),
        Road("Manila", "Bangkok", 2, ["red"], ["sea route"]),
        Road("Manila", "Jakarta", 2, ["grey"], ["sea route"]),
        Road("Bangkok", "Jakarta", 2, ["white"], ["sea route"]),
        Road("Jakarta", "Darwin", 2, ["black"], ["sea route"]),
        Road("Jakarta", "Perth", 3, ["grey"], ["sea route"]),
        Road("Darwin", "Perth", 2, ["red"], ["railway"]),
        Road("Darwin", "Sydney", 2, ["green"], ["railway"]),
        Road("Darwin", "Port Moresby", 1, ["red"], ["sea route"]),
        Road("Sydney", "Port Moresby", 3, ["yellow"], ["sea route"]),
        Road("Perth", "Sydney", 2, ["white", "yellow"], ["railway"]),
        Road("Christchurch", "Sydney", 1, ["red", "white"], ["sea route"]),
    ]
    known_tickets = [
        Ticket("Boston", "Washington", 4),
        Ticket("Boston", "Montreal", 5),
        Ticket("Montreal", "Chicago", 5),
        Ticket("Boston", "Chicago", 9),
    ]
    berg = build_graph(roads)

