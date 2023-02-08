from itertools import combinations

def hasTraingle(V:int, g: list[list]) -> bool:
    
    vertexSet = [i for i in range(V)]

    for X in combinations(vertexSet, 3): # for each combination of 3 vertices
        c1 = X[0] in g[X[1]]
        c2 = X[1] in g[X[2]]
        c3 = X[2] in g[X[0]]
        if c1 and c2 and c3: # if the 3 vertices form a triangle
            return True
    
    return False