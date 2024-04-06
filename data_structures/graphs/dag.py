import unittest


class DAGNode:
    def __init__(self, value: str):
        self.value = value
        self.children = []

    def add_child(self, child: "DAGNode") -> None:
        self.children.append(child)


class DAG:
    def __init__(self):
        self.nodes: dict[str, DAGNode] = {}

    def add_node(self, value: str) -> None:
        node = DAGNode(value)
        self.nodes[value] = node

    def add_edge(self, parent: str, child: str) -> None:
        if parent not in self.nodes:
            self.add_node(parent)
        if child not in self.nodes:
            self.add_node(child)
        self.nodes[parent].add_child(self.nodes[child])

    def get_children(self, node: str) -> list[str]:
        if node in self.nodes:
            return [child.value for child in self.nodes[node].children]
        return []

    def get_parents(self, node: str) -> list[str]:
        parents = []
        for key, value in self.nodes.items():
            if node in [child.value for child in value.children]:
                parents.append(key)
        return parents

    def topological_sort(self) -> list[str]:
        stack = []
        visited = set()

        def visit(node: DAGNode) -> None:
            if node.value not in visited:
                visited.add(node.value)
                for child in node.children:
                    visit(child)
                stack.append(node.value)

        for node in self.nodes.values():
            visit(node)

        return stack[::-1]

    def is_acyclic(self) -> bool:
        def has_cycle(node: DAGNode, visited: set[str], rec_stack: set[str]) -> bool:
            visited.add(node.value)
            rec_stack.add(node.value)

            for child in node.children:
                if child.value not in visited:
                    if has_cycle(child, visited, rec_stack):
                        return True
                elif child.value in rec_stack:
                    return True

            rec_stack.remove(node.value)
            return False

        visited = set()
        rec_stack = set()

        for node in self.nodes.values():
            if node.value not in visited:
                if has_cycle(node, visited, rec_stack):
                    return False

        return True

    def get_path(self, source: str, target: str) -> list[list[str]]:
        paths = []

        def dfs(node: DAGNode, path: list[str]) -> None:
            if node.value == target:
                paths.append(path)
            else:
                for child in node.children:
                    dfs(child, path + [child.value])

        if source in self.nodes and target in self.nodes:
            dfs(self.nodes[source], [source])

        return paths


class DAGTestCase(unittest.TestCase):
    def setUp(self):
        self.dag = DAG()
        self.dag.add_edge("A", "B")
        self.dag.add_edge("A", "C")
        self.dag.add_edge("B", "D")
        self.dag.add_edge("B", "E")
        self.dag.add_edge("C", "E")
        self.dag.add_edge("D", "F")
        self.dag.add_edge("E", "F")

    def test_topological_sort(self):
        expected = ["A", "C", "B", "E", "D", "F"]
        result = self.dag.topological_sort()
        self.assertEqual(result, expected)

    def test_is_acyclic(self):
        self.assertTrue(self.dag.is_acyclic())
        self.dag.add_edge("F", "A")  # Add a cycle
        self.assertFalse(self.dag.is_acyclic())

    def test_get_path(self):
        expected = [["A", "B", "D", "F"], ["A", "B", "E", "F"], ["A", "C", "E", "F"]]
        result = self.dag.get_path("A", "F")
        self.assertEqual(result, expected)

    def test_print_path_invalid_vertices(self):
        result = self.dag.get_path("A", "G")  # Invalid target vertex
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
