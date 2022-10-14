import networkx as nx
import sys
filepath = sys.argv[1]

fp = open("graph.txt", "w")

setG = nx.read_graph6(filepath)

fp.write(str(len(setG)))
fp.write("\n")

for G in setG:
    fp.write(str(len(G.nodes())) + " " + str(len(G.edges())))
    fp.write("\n")
    for edge in G.edges() :
        fp.write(str(edge[0]))
        fp.write(" ")
        fp.write(str(edge[1]))
        fp.write("\n")
    #print("connected?",nx.is_connected(G))
