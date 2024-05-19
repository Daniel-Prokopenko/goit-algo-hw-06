import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
edge_list = [
    ("A", "B", 5),
    ("B", "C", 3),
    ("C", "D", 4),
    ("D", "E", 2),
    ("E", "O", 6),
    ("C", "F", 7),
    ("F", "G", 15),
    ("G", "I", 3),
    ("I", "H", 5),
    ("H", "O", 4),
    ("G", "J", 2),
    ("J", "K", 6),
    ("K", "L", 3),
    ("K", "X", 3),
    ("X", "Y", 1),
    ("Y", "Z", 6),
    ("Y", "M", 6),
    ("L", "M", 5),
    ("M", "N", 2),
    ("C", "T", 6),
]


for edge in edge_list:
    source, target, weight = edge
    G.add_edge(source, target, weight=weight)


node_degrees = nx.degree(G)
for node, degree in node_degrees:
    print(f"Degree of node {node}: {degree}")
print("\n")
print(f"Amount of nodes: {len(G.nodes)}")
print(f"Amount of edges: {len(G.edges)}")
print("\n")

# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=10)
# labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# plt.show()


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph.neighbors(vertex)) - visited)

    bfs_recursive(graph, queue, visited)


print("Distances:")
distances_from_A = dijkstra(G, "A")
print(distances_from_A)
print("\n\nDFS:")
dfs_recursive(G, "A")
print("\n\nBFS:")
bfs_recursive(G, deque(["A"]))
