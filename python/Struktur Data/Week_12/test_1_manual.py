class Graph_1_Manual:
    def __init__(self, node : list, edge : list[tuple]):
        self.node = node
        self.edge = edge

nodes = [1, 2, 3]
edges = [(1, 2), (2, 3)]

graph = Graph_1_Manual(nodes, edges)

print("Nodes:", graph.node)
print("Edges:", graph.edge)
