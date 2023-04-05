import networkx as nx

import sys
sys.path.append("/Users/karthikjp/Desktop/MNS-vs-MCS/VI SEM/graphSearch") # add the parent directory to the path

import graphSearch.IG as IG

def find_cliques(G):
    cliques = []
    for clique in nx.find_cliques(G):
        cliques.append(clique)
    return cliques

# visit all the vertices in a clique, for each vertex which are not yet visited if it is maximal
def basic(V:int, edges:list[list]) -> bool:
    G = nx.Graph()
    nodes = []
    for i in range(V):
        nodes.append(i)
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)    
    adjacentList = [[] for i in range(V)]
    for edge in edges:
        adjacentList[edge[0]].append(edge[1])
        adjacentList[edge[1]].append(edge[0])
    maximalCliques = find_cliques(G)
    for clique in maximalCliques:
        labels = [[] for i in range(V)]
        for vk in clique:
            for ng in adjacentList[vk]:
                if ng not in clique:
                    labels[ng].append(vk)
        maximal = [False for i in range(V)]
        for v in range(V):
            if v in clique:
                continue
            isMaximal = True
            for other in range(V):
                if other != v and other not in clique:
                    isSubset = True 
                    for ele in labels[v]:
                        if ele not in labels[other]:
                            isSubset = False
                            break
                    if isSubset == True:
                        isMaximal = False
                        break
            if isMaximal == True:
                maximal[v] = True
        for v1 in range(V):
            for v2 in range(V):
                if v1 not in clique and v2 not in clique and v1 != v2 and maximal[v1] and maximal[v2]:
                    if len(labels[v1])>0 and len(labels[v2])>0:
                        if len(labels[v1]) != len(labels[v2]):
                            return True
    return False
            

# complex
def conjecture(V:int, edges:list[list]) -> bool:
    G = nx.Graph()
    nodes = []
    for i in range(V):
        nodes.append(i)
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)    
    adjacentList = [[] for i in range(V)]
    for edge in edges:
        adjacentList[edge[0]].append(edge[1])
        adjacentList[edge[1]].append(edge[0])
    maximalCliques = find_cliques(G)
    for clique in maximalCliques:
        for v in range(V):
            isVvalid = False
            if v not in clique:
                for vk in clique:
                    if vk in adjacentList[v]:
                        isVvalid = True
                        break
            if isVvalid:
                for u in range(V):
                    isUvalid = False  
                    if u not in clique and u != v and u in adjacentList[v]:
                        isUvalid = True
                    if isUvalid:
                        lastCliqueVertices = []
                        for vk in clique:
                            if vk not in adjacentList[v]:
                                lastCliqueVertices.append(vk)
                        for lastCliqueVertex in lastCliqueVertices:
                            finalCheck2 = True
                            for otherVertex in range(V):
                                if otherVertex not in clique and otherVertex != v:
                                    for ck in clique:
                                        if ck != lastCliqueVertex and otherVertex in adjacentList[ck] and otherVertex in adjacentList[v]:
                                            finalCheck2 = False
                                            break
                            if finalCheck2 == False:
                                continue
                            neighbourofVK = len(clique)-1
                            neighborsOfU = 1
                            for vk in clique:
                                if vk in adjacentList[u] and vk != lastCliqueVertex:
                                    neighborsOfU += 1
                            if neighbourofVK > neighborsOfU:
                                return True                
    return False


def getInput(filename):

    fp = open(filename, "r")
   
    if fp:

        numGraphs = int(fp.readline())

        cntIG = 0
        cntTree = 0
        cntNIG = 0
        cnt = 0

        for i in range(numGraphs):

            s = fp.readline().strip().split(" ")
            V, E = int(s[0]), int(s[1])
            edges = []
            for j in range(E):
                t = fp.readline().strip().split(" ")
                t[0], t[1] = int(t[0]), int(t[1])
                edges.append(t)
            
            if E == V-1:
                cntTree += 1
            if IG.isInteresting(V, E, edges) == True:
                cntIG += 1
            else:
                if E > V-1:
                    cntNIG += 1

            if basic(V, edges) == True:
                continue

            if conjecture(V, edges) == False and E > V-1:
                print("alert", i)
                cnt += 1

        print()
        print("Total number of nonIntersting graphs obs:", cnt)
        print()
        print("Total number of interesting graphs:", cntIG)
        print("Total number of trees:", cntTree)
        print("Total number of nonInteresting graphs:", cntNIG)

getInput(sys.argv[1])