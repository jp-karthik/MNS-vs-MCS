import networkx as nx
import sys

# find all cliques in a graph

def find_cliques(G):
    cliques = []
    for clique in nx.find_cliques(G):
        cliques.append(clique)
    return cliques

# pass a sample graph to the function find_cliques

def check_clique(G, clique):
    for i in range(len(clique)):
        for j in range(i+1, len(clique)):
            if not G.has_edge(clique[i], clique[j]):
                return False
    return True



G = nx.Graph()

# add vertices to the graph
G.add_nodes_from([1,2,3,4])
# add edges to the graph
G.add_edges_from([(1,2),(1,3),(2,3),(3,4), (4,1), (4,2)])



print(G)
print(find_cliques(G))

def getInput(filename):
    
    fp = open(filename, "r")

    if fp: # if the file is opened successfully

        numGraphs = int(fp.readline())
        
        cnt=0 # count the number of interesting graphs which are chordal

        for i in range(numGraphs):

            s = fp.readline().strip().split(" ")

            V, E = int(s[0]), int(s[1])
            
            edges = []
            
            for j in range(E):
                t = fp.readline().strip().split(" ")
                t[0], t[1] = int(t[0]), int(t[1])
                edges.append(t)
            
            # if IG.isInteresting(V, E, edges) == True and E > V-1:
            #     print("idx: ", i)
            #     cnt += 1

        print(cnt)

getInput(sys.argv[1])