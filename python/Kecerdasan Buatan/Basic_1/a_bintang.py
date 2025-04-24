import heapq

class Node:
    def __init__(self, name, g, h):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, neighbors, heuristic):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.name)

        for neighbor, weight in neighbors[current_node.name]:
            if neighbor in closed_list:
                continue
            g = current_node.g + weight
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, g, h)
            neighbor_node.parent = current_node
            heapq.heappush(open_list, neighbor_node)

    return None

neighbors = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}

start = 'A'
goal = 'D'
path = a_star(start, goal, neighbors, heuristic)
print("Path found:", path)