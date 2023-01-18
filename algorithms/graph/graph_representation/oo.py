class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight):
        self.edges[vertex] = weight


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph_dict[from_vertex].add_edge(to_vertex, weight)


# Create vertex instances
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')

# Create a new graph and add the vertex instances
g = Graph()
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)

# Add edges between the vertices
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'D', 4)

print(g.graph_dict)
# Output: {'A': <__main__.Vertex object at 0x7f3f3e3c6f50>,
#          'B': <__main__.Vertex object at 0x7f3f3e3c6f90>,
#          'C': <__main__.Vertex object at 0x7f3f3e3c6fd0>,
#          'D': <__main__.Vertex object at 0x7f3f3e3c6e50>}
