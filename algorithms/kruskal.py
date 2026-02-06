import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ejecutar_kruskal(csv_path="data/grafo.csv", output_path="outputs/kruskal_mst.png"):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    try:
        df = pd.read_csv(csv_path, header=0)
    except Exception:
        df = pd.read_csv(csv_path, header=None)
    cols = list(df.columns)
    u_col, v_col, w_col = cols[0], cols[1], cols[2]
    edges = []
    for _, row in df.iterrows():
        w = float(row[w_col])
        edges.append((row[u_col], row[v_col], w))
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    T = nx.minimum_spanning_tree(G, algorithm="kruskal")
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10)
    other_edges = [e for e in G.edges(data=True) if not T.has_edge(e[0], e[1])]
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in other_edges], alpha=0.3)
    mst_edges = [(u, v) for u, v in T.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2.5)
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()
    total_weight = sum(d["weight"] for _, _, d in T.edges(data=True))
    print("Kruskal MST total weight:", total_weight)
    print("Kruskal MST edges:")
    for u, v, d in T.edges(data=True):
        print(u, v, d["weight"])

if __name__ == "__main__":
    ejecutar_kruskal()
