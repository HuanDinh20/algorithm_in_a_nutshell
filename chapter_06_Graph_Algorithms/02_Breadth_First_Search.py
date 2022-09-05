"""
Breadth-First Search takes a different approach from Depth-First Search when
searching a graph. Breadth-First Search systematically visits all vertices in the
graph G = (V, E) that are k edges away from the source vertex s before visiting any
vertex that is k + 1 edges away. This process repeats until no more vertices are
reachable from s. Breadth-First Search does not visit vertices in G that are not
reachable from s. The algorithm works for undirected as well as directed graphs.
Breadth-First Search is guaranteed to find the shortest path in the graph from ver‐
tex s to a desired target vertex, although it may evaluate a rather large number of
nodes as it operates. Depth-First Search tries to make as much progress as possible,
and may locate a path more quickly, which may not be the shortest path.

**************** Input - Output ********************


"""

import collections


def bsf(graph, root):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)


if __name__ == '__main__':
    graph = {
        0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0], 4: [2]
    }
    bsf(graph, 0)