class Graph_1_Dinamis:
    def __init__(self):
        self.node = []
        self.edge = []

    def input_node(self):
        jumlah_node = int(input("Masukkan jumlah node: "))
        for i in range(jumlah_node):
            n = int(input(f"Masukkan node ke-{i+1}: "))
            self.node.append(n)

    def input_edge(self):
        self.edge = []
        for i in range(len(self.node) - 1):
            self.edge.append((self.node[i], self.node[i+1]))

    def tampilkan_graph(self):
        print("\n=== GRAPH ===")
        print("Nodes:", self.node)
        print("Edges:", self.edge)

if __name__ == "__main__":
    graph = Graph_1_Dinamis()
    graph.input_node()
    graph.input_edge()
    graph.tampilkan_graph()
