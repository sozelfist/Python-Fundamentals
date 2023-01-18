from typing import List


def johnson(adj_matrix: List[List[int]], start: int, goal: int) -> List[int]:
    n = len(adj_matrix)
    dist = [float('inf')] * n
    dist[start] = 0
    queue = [start]
    while queue:
        u = queue.pop(0)
        for v in range(n):
            if adj_matrix[u][v] != float('inf'):
                if dist[v] > dist[u] + adj_matrix[u][v]:
                    dist[v] = dist[u] + adj_matrix[u][v]
                    queue.append(v)
    if dist[goal] != float('inf'):
        return dist[goal]
    else:
        return []
