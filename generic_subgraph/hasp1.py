from mns import MNS
from mcs import MCS
from itertools import permutations, combinations
from isInteresting import isInteresting
import sys

def P1(v:int, g:list[list], s:list) -> True: # check for the general subgraph condition
    # a->0,b->1,c->2,d->3,e->4,g->adjList,s->sequence
    c1 =  g[s[3]].count(s[0])>0 and g[s[1]].count(s[0])>0 and g[s[1]].count(s[2])>0 and g[s[1]].count(s[4])>0 and g[s[2]].count(s[4])>0 # all required edges
    c2 = True # no common neighbour between a and b
    c3 = True # no common neighbour between a and c
    c4 = True # no common neighbour between a and e
    c5 = not (g[s[2]].count(s[0])>0 and g[s[4]].count(s[0])>0) # (a,c) and (a,e) is not in E(G)
    for node in range(v):
        if g[node].count(s[0])>0 and g[node].count(s[1])>0 and node!=s[2] and node!=s[4]:
            c2 = False
        if g[node].count(s[0])>0 and g[node].count(s[2])>0 and node!=s[1]:
            c3 = False
        if g[node].count(s[0])>0 and g[node].count(s[4])>0 and node!=s[1]:
            c4 = False
    finalCnd = c1 and c2 and (c3 or c4) and c5
    return True if finalCnd else False