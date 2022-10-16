#include<bits/stdc++.h>
using namespace std;

class MCS {
public:
    int V;
    int E;
    vector<vector<int>> adjList;
    vector<bool> isVisited;
    vector<set<int>> MCSsets;
    vector<vector<int>> MCS_orderings;
    // contructor
    MCS(int V, int E, vector<pair<int, int>>& edges) {
        this->V = V;
        this->E = E;
        adjList.resize(V);
        isVisited.resize(V, false);
        MCSsets.resize(V, {});
        for (int i = 0; i < E; i++) {
            adjList[edges[i].first].push_back(edges[i].second);
            adjList[edges[i].second].push_back(edges[i].first);
        }
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
                    // explore
                    performMCS(ordering);
                    // backtrack
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
    void performAllPossible() {
        vector<int> ordering;
        for (int i = 0; i < V; i++) {
            MCSsets[i].insert(V + 1);
            performMCS(ordering);
            MCSsets[i].erase(V + 1);
        }
    }
    int getSize() {
        return this->MCS_orderings.size();
    }
};
