V = int(input()) # number of vertices
E = int(input()) # number of edges

MNSset = [[] for _ in range(V)] # sets defined for each vertices (during MNS search)
MCSset = [[] for _ in range(V)] # sets defined for each vertices (during MCS search)

adjList = [[] for i in range(V)]

for i in range(E) : 
    edge = input().split()
    edge = [int(x) for x in edge]
    adjList[edge[0]].append(edge[1])
    adjList[edge[1]].append(edge[0])


