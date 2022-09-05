"""
******************* Depth-First Search Summary ************
Best, Average, Worst: O(V+E)

depthFirstSearch(G, s):
    for v in V do:
        pred[v] = -1
        color[v] = White (1)
    dfsVists(s)
end

dfsVisits(u):
    color[u] = Gray
    for neighbor v of u:
        if color[v] = White: (2)
            pred[v] = u
            dfsVisits(v)
    color[u] = Black    (3)

end

(1): Initially all vertices are marked as not visited.
(2): Find unvisited neighbor and head in that direction.
(3): Once all neighbors are visited, this vertex is done.

******* Graph
A graph G = (V, E) is defined by a set of vertices, V, and a set of edges, E, over pairs
of these vertices. There are three common types of graphs:
1. Undirected, unweighted graphs:
 - These model relationships between vertices (u, v) without regard for the direc‐
tion of the relationship. These graphs are useful for capturing symmetric infor‐
mation. For example, in a graph modeling a social network, if Alice is a friend
of Bob, then Bob is a friend of Alice
2. Directed graphs
- These model relationships between vertices (u, v) that are distinct from the
relationship between (v, u), which may or may not exist. For example, a pro‐
gram to provide driving directions must store information on one-way streets
to avoid giving illegal directions.
3. Weighted graphs:
These model relationships where there is a numeric value known as a weight
associated with the relationship between vertices (u, v). Sometimes these values
can store arbitrary non-numeric information. For example, the edge between
towns A and B could store the mileage between the towns, the estimated travel‐
ing time in minutes, or the name of the street or highway connecting
the towns.

The most highly structured of the graphs—a directed, weighted graph—defines a
nonempty set of vertices {v0, v1, …, vn−1}, a set of directed edges between pairs of
distinct vertices (such that every pair has at most one edge between them in each
direction), and a positive weight associated with each edge. In many applications,
the weight is considered to be a distance or cost. For some applications, we may
want to relax the restriction that the weight must be positive (e.g., a negative weight
could reflect a loss, not a profit), but we will be careful to declare when
this happens.




As its name implies, depth-first search searches <deeper= in the graph whenever
possible. Depth-first search explores edges out of the most recently discovered
vertex v that still has unexplored edges leaving it. Once all of v’s edges have been
explored, the search <backtracks= to explore edges leaving the vertex from which v
was discovered. This process continues until all vertices that are reachable from the
original source vertex have been discovered. If any undiscovered vertices remain,
then depth-ûrst search selects one of them as a new source, repeating the search
from that source. The algorithm repeats this entire process until it has discovered
every vertex.

Initially, each vertex is colored white to represent that it has not yet been visited,
and Depth-First Search invokes dfsVisit on the source vertex, s. dfsVisit(u) col‐
ors u gray before recursively invoking dfsVisit on all adjacent vertices of u that
have not yet been visited (i.e., they are colored white).  Once these recursive calls
have completed, u can be colored black, and the function returns.  When the recur‐
sive dfsVisit function returns, Depth-First Search backtracks to an earlier vertex
in the search (indeed, to a vertex that is colored gray), which may have an unvisited
adjacent vertex that must be explored.

Depth-First Search has no global awareness of the graph, and so it will blindly
search the vertices <5, 6, 7, 8>, even though these are in the wrong direction from
the target, t. Once Depth-First Search completes, the pred[] values can be used to
generate a path from the original source vertex, s, to each vertex in the graph.
Note that this path may not be the shortest possible path;

************ Input/Output ******************
The input is a graph G = (V, E) and a source vertex s ∈ V representing the start
location.
Depth-First Search produces the pred[v] array that records the predecessor vertex
of v based on the depth-first search ordering.

*********** Contex *************
Depth-First Search only needs to store a color (either white, gray, or black) with
each vertex as it traverses the graph. Thus, Depth-First Search requires only O(n)
overhead in storing information while it explores the graph starting from s.

Depth-First Search can store its processing information in arrays separately from
the graph. Depth-First Search only requires that it can iterate over the vertices in a
graph that are adjacent to a given vertex. This feature makes it easy to perform
Depth-First Search on complex information, since the dfsVisit function accesses
the original graph as a read-only structure

**** Solution

"""
graph = {
    "A" : ["B", "C", "D"], "B": ["E"], "C": ["D", "E"], "D": [], "E":[]
}
visited = set()


def dfs(visited_nodes, graph_data, root):
    if root not in visited_nodes:
        print("root: ", root)
        visited_nodes.add(root)
        for neighbors in graph_data[root]:
            dfs(visited_nodes, graph_data, neighbors)


dfs(visited, graph, "A")


