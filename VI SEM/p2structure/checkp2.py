import sys
from p2 import hasP2 # import the function hasP2 from p2.py

def getInput() -> None:

    IPfile = sys.argv[1]
    
    fp = open(IPfile, "r")
    numGraphs = int(fp.readline())
    
    cnt=0 # count the number of graphs that do not have a P2 structure
    
    for i in range(numGraphs):
    
        s = fp.readline().strip().split(" ")
    
        V, E = int(s[0]), int(s[1]) # read the number of vertices and edges
        edges = [] # list of edges
        adjList=[[] for i in range(V)] # adjacency list
    
        for j in range(E): # read the edges
            t = fp.readline().strip().split(" ")
            t[0], t[1] = int(t[0]), int(t[1])
            edges.append(t)
    
        for edge in edges: # create the adjacency list
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
    
        if hasP2(V, adjList)==False: # if the graph does not have a P2 structure print
            print(i, "is the black sheep")
            cnt+=1 
    
    print(cnt)

getInput()