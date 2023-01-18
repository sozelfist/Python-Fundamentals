# Creating a directed graph using an adjacency list
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)

    def print_graph(self):
        print(self.adj_list)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_graph()
# Output: [[1, 2], [2], [0, 3], []]
