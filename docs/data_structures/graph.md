## Graph

## Implementation

The `Graph` class is implemented here [graph.py](../../data_structures/graph.py)

## Explanation

This code defines a class `Graph` that represents a simple graph data structure. A graph can be either directed or undirected, and this is determined by the directed parameter passed during initialization. The class has several methods that allow the user to add vertices and edges to the graph, and retrieve information about the graph's vertices and edges.

- The `add_vertex` method adds a new vertex to the graph. If the vertex does not already exist in the graph, it is added with an empty list of edges.

- The `add_edge` method onnects two vertices in the graph. It takes in two vertex numbers, `vertex1` and `vertex2`, and creates an edge between them. If the graph is `directed`, the edge is created from `vertex1` to `vertex2`. If it's `undirected`, edges are created between `vertex1` and `vertex2`.

- The `get_vertices` method returns a list of all the vertices in the graph.

- The `get_edges` method returns a dictionary that represents the graph's edges. The keys of the dictionary are the vertices, and the values are lists of the vertices that the key vertex is connected to.

- The `__str__` and `__repr__` methods return the string representation of the graph in the format of a dictionary where the keys are the vertices and the values are the lists of adjacent vertices.

The class also defines a `TestGraph` subclass that runs a set of test cases to check if the methods of the `Graph` class are working properly. The test cases include adding vertices, edges, and checking if the vertices and edges are stored correctly in the graph.