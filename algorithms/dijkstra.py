import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def ejecutar_dijkstra(nodo_origen, csv_path="data/grafo.csv", output_path="outputs/dijkstra_paths.png"):
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

    if nodo_origen not in G.nodes:
        print("Nodo origen no existe en el grafo.")
        return

    distancias = nx.single_source_dijkstra_path_length(G, nodo_origen)
    caminos = nx.single_source_dijkstra_path(G, nodo_origen)

    for nodo, distancia in distancias.items():
        print("Distancia a", nodo, "=", distancia)
    print("Rutas desde", nodo_origen)
    for nodo, camino in caminos.items():
        print(nodo, ":", camino)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))

    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10)

    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.3)

    for destino, camino in caminos.items():
        path_edges = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5)

    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()

if __name__ == "__main__":
    ejecutar_dijkstra("A")
