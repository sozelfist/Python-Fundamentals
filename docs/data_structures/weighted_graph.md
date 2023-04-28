# Weighted Graph

A weighted graph or a network is a graph in which a number (the weight) is assigned to each edge. Such weights might represent for example costs, lengths or capacities, depending on the problem at hand. Such graphs arise in many contexts, for example in shortest path problems such as the traveling salesman problem.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Weighted_network.svg/220px-Weighted_network.svg.png">
    <p>A weighted graph with ten vertices and twelve edges</p>
</div>

## Implementation

The `WeightedGraph` class is implemented here [weighted_graph.py](../../data_structures/weighted_graph.py)

## Explanation

This code defines a class `WeightedGraph` that represents a weighted graph data structure. A weighted graph is a graph that has weights or values associated with each edge.

The class `WeightedGraph` has the following methods:

- `__init__(self, directed: bool = False)` : constructor which creates an empty graph and sets the `directed` attribute to the value passed in.
- `add_vertex(self, vertex: int) -> None` : adds a new `vertex` to the graph. If the vertex is not already present in the graph, it is added as a key to the graph dictionary with an empty dictionary as its value.
- `add_edge(self, vertex1: int, vertex2: int, weight: int) -> None` : adds a new edge between `vertex1` and `vertex2` with the given `weight`. If the edge is `directed`, it only adds the edge from vertex1 to vertex2. If the edge is `undirected`, it adds edges from both vertices to each other.
- `get_vertices(self) -> List[int]` : returns a list of all the vertices in the graph.
- `get_edges(self) -> Dict[int, Dict[int, int]]` : returns a dictionary representation of the graph, where the keys are the vertices, and the values are the edges and their weights.

The class also includes a `TestWeightedGraph` test case class that tests the above methods of the `WeightedGraph` class using the `unittest` module.

In the `setUp()` method of the `TestWeightedGraph` class, an object of the `WeightedGraph` class is created, and 3 vertices are added to it. Then, 2 edges are added between the vertices, each with a weight. The test methods of the class check if the methods of the `WeightedGraph` class are working correctly.