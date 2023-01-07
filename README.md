> ## <h2 align=center>Maximal Neighbourhood Search V/S Maximum Cardinality Search</h2>

> ### <h3 align=center>Abstract</h3>

<p>
Graph searching is considered as one of the most essential and widely used tools in graph algorithms.
Given a graph G, a graph search is a method of transversing the vertices of the graph V (G) and storing
them in a sequence σ, which is termed as a vertex ordering for the graph G. Also, for the purpose of
simplicity, consider G as connected. Every prefix of the obtained vertex ordering σ will form a vertex
induced subgraph of G which must be connected.
</p>
<p>
By defining some specific rule for the selection of the vertices, various different graph search methods
are defined. Two of the common known search methods are Depth First Search (DFS) and Breadth First
Search (BFS). In the project, we deal with two other graph search algorithms - Maximal Neighbourhood
Search (MNS) and Maximum Cardinality Search (MCS).
</p>

> <strong><em>MNS algorithm:</em></strong> Begin with a starting vertex s ∈ V (G), set its label as {n + 1}, where n = |V (G)|
and set the label for all other vertices in V (G) as ϕ (empty set {.}). In the k th iteration (k ∈ {1, ..., n}),
choose the k th vertex u such that it is not yet selected and the label corresponding to u is maximal (under
set inclusion), then add u to the vertex ordering σ and insert element k into to the labels of all its non
selected neighbours. Repeat the same process until all the vertices of the graph G are added to the vertex
ordering σ.

> <strong><em>MCS algorithm:</em></strong> Begin with a starting vertex s ∈ V (G), set its label as {n + 1}, where n = |V (G)|
and set the label for all other vertices in V (G) as ϕ (empty set {.}). In the k th iteration (k ∈ {1, ..., n}),
choose the k th vertex u such that it is not yet selected and the label corresponding to u has maximum
number of elements in it (cardinality of the label is maximum), then add u to the vertex ordering σ and
insert element k into to the labels of all its non selected neighbours. Repeat the same process until all
the vertices of the graph G are added to the vertex ordering σ.

<p>
It is evident that every valid MCS vertex ordering gives a valid MNS vertex ordering for any connected
graph because MNS is a more generalized version of MCS. But the converse may not be true for some of
the connected graphs.
</p>
<p>
Our aim is to find the class of graphs for which MCS and MNS are equivalent. Two graph searches
methods are considered equivalent on a graph G if the lists of vertex ordering sequences produced by both
of them are the same. Conceptually, there should not exist any valid MNS ordering σ which is not a valid
MCS ordering. If this is the case, then we can say that the two search methods are indistinguishable on
this graph G.
</p>
