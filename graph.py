import networkx as nx
import matplotlib.pyplot as plt


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

print(f"Amount of nodes: {len(G.nodes)}")
print(f"Amount of edges: {len(G.edges)}")


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=10)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()


dfs_tree = nx.dfs_tree(G, source="A")
print("DFS Tree:", dfs_tree.edges())

bfs_tree = nx.bfs_tree(G, source="A")
print("BFS Tree:", bfs_tree.edges())

shortest_path_cost = nx.shortest_path_length(G, source="A", target="N", weight="weight")
shortest_path = nx.shortest_path(G, source="A", target="N", weight="weight")

print(shortest_path_cost)
print(shortest_path)
