from dataclasses import dataclass, field
import networkx as nx
from typing import List, Tuple, Set, Optional
from Models import Road, Ticket
from Data import roads, known_tickets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def build_graph(roads: List[Road]) -> nx.MultiGraph:
    Graph = nx.MultiGraph()
    for r in roads:
        if r.start.name not in Graph:
            Graph.add_node(r.start.name, wharf=r.start.wharf)
        if r.end.name not in Graph:
            Graph.add_node(r.end.name, wharf=r.end.wharf)
        for c in r.color:
            Graph.add_edge(r.start.name, r.end.name, weight=r.length, color=c, type=r.type)
    return Graph


def train_model(tickets: List[Ticket]) :
    graph = build_graph(roads)

    rows = []

    df = pd.DataFrame(rows)
    y = df["points"]

    X_train, X_test, y_train, y_test = train_test_split(tickets, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"MAE (test):  {mean_absolute_error(y_test, y_pred):.2f} bodov")
    print(f"R^2  (test): {r2_score(y_test, y_pred):.3f}")


    return model, graph

def generate_tickets(model, graph, feature_cols):

    return


if __name__ == "__main__":
    berg = build_graph(roads)
    train_model(known_tickets)
