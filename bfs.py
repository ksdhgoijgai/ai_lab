from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(adj, s):
    q = deque()
    visited = [False] * len(adj)
    visited[s] = True
    q.append(s)
    while q:
        curr = q.popleft()
        print(curr, end=" ")
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def visualize_graph(edges, num_nodes):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, font_color="black", edge_color="gray")
    plt.title("Graph Visualization")
    plt.show()

if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 4)
    ]
    for u, v in edges:
        add_edge(adj, u, v)
    print("BFS starting from 0:")
    bfs(adj, 0)
    visualize_graph(edges, V)
