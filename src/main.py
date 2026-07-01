from dataclasses import dataclass, field
import networkx as nx
from typing import List, Tuple, Set, Optional
from Models import Road, Ticket
from Roads import roads
from KnownTickets import known_tickets


def build_graph(roads: List[Road]) -> nx.MultiGraph:
    G = nx.MultiGraph()
    for r in roads:
        if r.start.name not in G:
            G.add_node(r.start.name, wharf=r.start.wharf)
        if r.end.name not in G:
            G.add_node(r.end.name, wharf=r.end.wharf)
        for c in r.color:
            G.add_edge(r.start.name, r.end.name, weight=r.length, color=c, type=r.type)
    return G


def train_model(G: nx.MultiGraph, tickets: List[Ticket]):
    return


if __name__ == "__main__":
    berg = build_graph(roads)
    train_model(berg, known_tickets)
