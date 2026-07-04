import networkx as nx
from typing import List
from Models import Road, Ticket
from Data import roads, known_tickets
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
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


def ticket_features(ticket: Ticket, graph: nx.MultiGraph, all_tickets: List[Ticket]):
    try:
        dist = nx.shortest_path_length(graph, ticket.start.name, ticket.end.name, weight="weight")
        path = nx.shortest_path(graph, ticket.start.name, ticket.end.name, weight="weight")
    except nx.NetworkXNoPath:
        return None

    start_wharf = int(ticket.start.wharf)
    end_wharf = int(ticket.end.wharf)
    start_degree = graph.degree(ticket.start.name)
    end_degree = graph.degree(ticket.end.name)
    start_ticket_count = sum(1 for t in all_tickets if t.start.name == ticket.start.name or t.end.name == ticket.start.name)
    end_ticket_count = sum(1 for t in all_tickets if t.start.name == ticket.end.name or t.end.name == ticket.end.name)

    sea_edges = 0
    hard_edges = 0
    for u, v in zip(path[:-1], path[1:]):
        edge_data = min(graph.get_edge_data(u, v).values(), key=lambda d: d["weight"])
        if "sea route" in edge_data["type"]:
            sea_edges += 1
        if "hard terrain railway" in edge_data["type"]:
            hard_edges += 1

    path_length_edges = len(path) - 1

    return {
        "distance": dist,
        "path_length_edges": path_length_edges,
        "avg_edge_length": dist / path_length_edges,
        "wharf_count": start_wharf + end_wharf,
        "degree_sum": start_degree + end_degree,
        "degree_min": min(start_degree, end_degree),
        "ticket_count_sum": start_ticket_count + end_ticket_count,
        "ticket_count_max": max(start_ticket_count, end_ticket_count),
        "sea_edges": sea_edges,
        "points": ticket.points,
    }


def build_dataset(tickets: List[Ticket], graph: nx.MultiGraph) -> pd.DataFrame:
    rows = [ticket_features(t, graph, tickets) for t in tickets]
    rows = [r for r in rows if r is not None]
    return pd.DataFrame(rows)


def split_by_city_frequency(tickets: List[Ticket], min_freq: int = 3):
    city_counts = Counter()
    for t in tickets:
        city_counts[t.start.name] += 1
        city_counts[t.end.name] += 1

    core_tickets = []
    rare_tickets = []
    for t in tickets:
        if city_counts[t.start.name] < min_freq or city_counts[t.end.name] < min_freq:
            rare_tickets.append(t)
        else:
            core_tickets.append(t)

    return core_tickets, rare_tickets


def compare_models(X, y, bins):
    """Porovna viacero modelov pomocou stratifikovaneho CV a vrati vysledky."""
    candidates = {
        "RandomForest depth=4": RandomForestRegressor(n_estimators=200, max_depth=4, min_samples_leaf=3, random_state=42),
        "RandomForest depth=6": RandomForestRegressor(n_estimators=100, max_depth=6, min_samples_leaf=2, random_state=42),
        "RandomForest depth=8": RandomForestRegressor(n_estimators=200, max_depth=8, min_samples_leaf=1, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.05, random_state=42),
        "Ridge (alpha=1)": Ridge(alpha=1.0),
        "Ridge (alpha=5)": Ridge(alpha=5.0),
        "LinearRegression": LinearRegression(),
    }

    results = []
    for name, model in candidates.items():
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        mae_list, r2_list = [], []
        for train_idx, test_idx in skf.split(X, bins):
            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mae_list.append(mean_absolute_error(y_test, y_pred))
            r2_list.append(r2_score(y_test, y_pred))

        mae_arr = np.array(mae_list)
        r2_arr = np.array(r2_list)
        results.append({
            "model": name,
            "MAE_mean": mae_arr.mean(),
            "MAE_std": mae_arr.std(),
            "R2_mean": r2_arr.mean(),
            "R2_std": r2_arr.std(),
        })

    df_results = pd.DataFrame(results).sort_values("R2_mean", ascending=False)
    return df_results


def train_model(tickets: List[Ticket], graph: nx.MultiGraph, min_freq: int = 3):
    core_tickets, rare_tickets = split_by_city_frequency(tickets, min_freq=min_freq)
    print(f"Core tickety: {len(core_tickets)}, Rare tickety (holdout): {len(rare_tickets)}")

    df_core = build_dataset(core_tickets, graph)
    feature_cols = [c for c in df_core.columns if c != "points"]
    X = df_core[feature_cols]
    y = df_core["points"]
    bins = pd.qcut(y, q=5, labels=False, duplicates="drop")

    print("\n=== Porovnanie modelov (core, stratified CV) ===")
    comparison = compare_models(X, y, bins)
    print(comparison.to_string(index=False))

    best_model_name = comparison.iloc[0]["model"]
    print(f"\nNajlepsi model podla R2: {best_model_name}")

    # Pouzi realne najlepsi model namiesto natvrdo RandomForest
    model_candidates = {
        "RandomForest depth=4": RandomForestRegressor(n_estimators=200, max_depth=4, min_samples_leaf=3, random_state=42),
        "RandomForest depth=6": RandomForestRegressor(n_estimators=100, max_depth=6, min_samples_leaf=2, random_state=42),
        "RandomForest depth=8": RandomForestRegressor(n_estimators=200, max_depth=8, min_samples_leaf=1, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=100, max_depth=3, learning_rate=0.05, random_state=42),
        "Ridge (alpha=1)": Ridge(alpha=1.0),
        "Ridge (alpha=5)": Ridge(alpha=5.0),
        "LinearRegression": LinearRegression(),
    }
    model = model_candidates[best_model_name]
    model.fit(X, y)

    print(f"\nFinalny model: {best_model_name}")

    # Feature importance len ak model ma coef_ alebo feature_importances_
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
        print("\nFeature importance:")
        for name, imp in sorted(zip(feature_cols, importances), key=lambda x: -x[1]):
            print(f"  {name}: {imp:.3f}")
    elif hasattr(model, "coef_"):
        print("\nKoeficienty (linearny model):")
        for name, coef in sorted(zip(feature_cols, model.coef_), key=lambda x: -abs(x[1])):
            print(f"  {name}: {coef:+.3f}")
        print(f"  intercept: {model.intercept_:.3f}")

    print("\nPriemerne points podla wharf_count:")
    print(df_core[["wharf_count", "points"]].groupby("wharf_count")["points"].agg(["mean", "count"]))

    if rare_tickets:
        df_rare = build_dataset(rare_tickets, graph)
        X_rare = df_rare[feature_cols]
        y_rare = df_rare["points"]
        y_rare_pred = model.predict(X_rare)

        mae_rare = mean_absolute_error(y_rare, y_rare_pred)
        r2_rare = r2_score(y_rare, y_rare_pred)

        print(f"\nMAE (rare holdout): {mae_rare:.2f} bodov")
        print(f"R^2  (rare holdout): {r2_rare:.3f}")
        print("\nPredikcie na rare ticketoch (skutocne vs predikovane):")
        for t, pred in zip(rare_tickets, y_rare_pred):
            print(f"  {t.start.name} -> {t.end.name}: skutocne={t.points}, predikovane={round(pred)}")

    return model, feature_cols


def generate_tickets(model, graph, feature_cols):
    return


if __name__ == "__main__":
    berg = build_graph(roads)
    train_model(known_tickets, berg, min_freq=3)