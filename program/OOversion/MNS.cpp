#include<bits/stdc++.h>
using namespace std;

class MNS {
public:
    int V;
    int E;
    vector<vector<int>> adjList;
    vector<bool> isVisited;
    vector<set<int>> MNSsets;
    vector<vector<int>> MNS_orderings;
    // constructor 
    MNS(int V, int E, vector<pair<int, int>>& edges) {
        this->V = V;
        this->E = E;
        adjList.resize(V);
        isVisited.resize(V, false);
        MNSsets.resize(V, {});
        for (int i = 0; i < E; i++) {
            adjList[edges[i].first].push_back(edges[i].second);
            adjList[edges[i].second].push_back(edges[i].first);
        }
    }
    // checking whether the set associated with the vertex is maximal under set inclusion (for MNS)
    bool isSetMaximal(int u) {
        bool isMaximal = true;
        for (int i = 0; i < V; i++) {
            if (i == u) continue;
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
                    // explore
                    performMNS(ordering);
                    //backtrack
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
    void performAllPossible() {
        vector<int> ordering;
        for (int i = 0; i < V; i++) {
            MNSsets[i].insert(V + 1);
            performMNS(ordering);
            MNSsets[i].erase(V + 1);
        }
    }
    int getSize() {
        return this->MNS_orderings.size();
    }
};
