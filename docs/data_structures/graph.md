## Graph

In computer science, a graph is an abstract data type that is meant to implement the undirected graph and directed graph concepts from the field of graph theory within mathematics.

A graph data structure consists of a finite (and possibly mutable) set of vertices (also called nodes or points), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as edges (also called links or lines), and for a directed graph are also known as edges but also sometimes arrows or arcs. The vertices may be part of the graph structure, or may be external entities represented by integer indices or references.

A graph data structure may also associate to each edge some edge value, such as a symbolic label or a numeric attribute (cost, capacity, length, etc.).

## Operartions

The basic operations provided by a graph data structure G usually include:

- `adjacent(G, x, y)`: tests whether there is an edge from the vertex x to the vertex y;
- `neighbors(G, x)`: lists all vertices y such that there is an edge from the vertex x to the vertex y;
- `add_vertex(G, x)`: adds the vertex x, if it is not there;
- `remove_vertex(G, x)`: removes the vertex x, if it is there;
- `add_edge(G, x, y, z)`: adds the edge z from the vertex x to the vertex y, if it is not there;
- `remove_edge(G, x, y)`: removes the edge from the vertex x to the vertex y, if it is there;
- `get_vertex_value(G, x)`: returns the value associated with the vertex x;
- `set_vertex_value(G, x, v)`: sets the value associated with the vertex x to v.
Structures that associate values to the edges usually also provide:

- `get_edge_value(G, x, y)`: returns the value associated with the edge (x, y);
- `set_edge_value(G, x, y, v)`: sets the value associated with the edge (x, y) to v.

## Common data structures for graph representation

- Adjacency list: Vertices are stored as records or objects, and every vertex stores a list of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.
- Adjacency matrix: A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.
- Incidence matrix: A two-dimensional matrix, in which the rows represent the vertices and columns represent the edges. The entries indicate the incidence relation between the vertex at a row and edge at a column.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/220px-6n-graf.svg.png">
    <p>A graph with six vertices and seven edges</p>
</div>

## Types of Graph

In graph theory, there are several types of graphs. Some of the most common types of graphs are:

- **Undirected Graph**: A graph in which edges have no orientation.
- **Directed Graph**: A graph in which edges have orientation.
- **Weighted Graph**: A graph in which a number (the weight) is assigned to each edge.
- **Complete Graph**: A graph in which each pair of vertices is connected by an edge.
- **Bipartite Graph**: A graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set.
- **Cyclic Graph**: A graph that contains at least one cycle (a path that starts and ends at the same vertex).
- **Acyclic Graph**: A graph that contains no cycles.
- **Connected Graph**: A graph in which there is a path between any two vertices.
- **Disconnected Graph**: A graph that is not connected.

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