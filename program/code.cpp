// header files
#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>

using namespace std;

static int V; // # of vertices
static int E; // # of edges 

// adjacancy list 
vector<vector<int>> adjList;

// sets assigned as label to each vertex of the graph
vector<set<int>> MNSsets; 
vector<set<int>> MCSsets;

// visited array to keep track of already visited elements
vector<int> isVisited;

// stores all the possible valid MNS and MCS orderings respectively
vector<vector<int>> MNS_orderings;
vector<vector<int>> MCS_orderings;

// checking whether the set associated with the vertex is maximal under set inclusion (for MNS)
bool isSetMaximal(int u) {
    bool isMaximal = true;
    for (int i = 0; i < V && i != u; i++) {
        if (!isVisited[i]) {
            if (MNSsets[u].size() == MNSsets[i].size()) continue;
            bool isSubset = true;
            for (int element : MNSsets[u]) {
                if (MNSsets[i].count(element) == 0) {
                    isSubset = false;
                }
            }
            if (!isSubset) {
                continue;
            } else {
                isMaximal = false;
                break;
            }
        }
    }
    return isMaximal;
}

// checking whether the set associated with the vertex is maximal under set inclusion and has maximum cardinality (for MCS)
bool isSetMaximalCardinality(int u) {
    int maxSize = 0;
    for (int i = 0; i < V; i++) {
        if (!isVisited[i]) {
            maxSize = max(maxSize, (int) MCSsets[i].size());
        } 
    }
    if (MCSsets[u].size() == maxSize) return true;
    else return false;
}

// MNS algorithm
void performMNS(vector<int>& ordering) {
    if (ordering.size() == V) {
        MNS_orderings.push_back(ordering);
        return;
    }
    for (int i = 0; i < V; i++) {
        if (!isVisited[i]) {
            if (MNSsets[i].size() > 0 && isSetMaximal(i)) {
                isVisited[i] = true;
                ordering.push_back(i);
                for (int neighbour : adjList[i]) {
                    if (!isVisited[neighbour]) {
                        MNSsets[neighbour].insert(ordering.size());
                    }
                } 
                performMNS(ordering);
                for (int neighbour : adjList[i]) {
                    if (!isVisited[neighbour]) {
                        MNSsets[neighbour].erase(ordering.size());
                    }
                }
                isVisited[i] = false;
                ordering.pop_back();
            } 
        }
    }    
}

// MCS algorithm
void performMCS(vector<int>& ordering) {
    if (ordering.size() == V) {
        MCS_orderings.push_back(ordering);
        return;
    }
    for (int i = 0; i < V; i++) {
        if (!isVisited[i]) {
            if (MCSsets[i].size() > 0 && isSetMaximalCardinality(i)) {
                isVisited[i] = true;
                ordering.push_back(i);
                for (int neighbour : adjList[i]) {
                    if (!isVisited[neighbour]) {
                        MCSsets[neighbour].insert(ordering.size());
                    }
                } 
                performMCS(ordering);
                for (int neighbour : adjList[i]) {
                    if (!isVisited[neighbour]) {
                        MCSsets[neighbour].erase(ordering.size());
                    }
                }
                isVisited[i] = false;
                ordering.pop_back();
            } 
        }
    }    
}

int main() {
    cin >> V >> E;
    adjList.resize(V);

    // none of the vertices are visited, so isVisited[u] is false for all u in vertex set
    isVisited.resize(V, false);

    // initialize each set correspoding to a set to a null set
    MCSsets.resize(V, {}); 
    MNSsets.resize(V, {});

    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        // vertices are zero indexed
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    int startVertex;
    vector<int> ordering;

    // perform MNS for all possible starting vertices
    for (int i = 0; i < V; i++) {
        startVertex = i;
        MNSsets[startVertex].insert(V + 1);
        performMNS(ordering);
        MNSsets[startVertex].erase(V + 1);
    }

    // perform MCS for all possible starting vertices
    for (int i = 0; i < V; i++) {
        startVertex = i;
        MCSsets[startVertex].insert(V + 1);
        performMCS(ordering);
        MCSsets[startVertex].erase(V + 1);
    }

    cout << "# of valid MNS ordering is : " << MNS_orderings.size() << endl;
    cout << "# of valid MCS ordering is : " << MCS_orderings.size() << endl;

    return 0;
}