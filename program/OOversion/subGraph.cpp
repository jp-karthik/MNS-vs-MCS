// header files
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include "MNS.cpp"
#include "MCS.cpp"
using namespace std;

bool isInteresting(int V, int E, vector<pair<int,int>>& edges) {
    MNS* mns = new MNS(V, E, edges);
    MCS* mcs = new MCS(V, E, edges);
    mns->performAllPossible();
    mcs->performAllPossible();
    int mnsSize = mns->getSize();
    int mcsSize = mcs->getSize();
    delete mns;
    delete mcs;
    if (mnsSize == mcsSize) return false;
    else return true;
}

// taking in a graph and return true if there is no Interesting vertex induced subgraph
bool allSubgraph(int V, int E, vector<pair<int,int>>& edges) {
    bool valid = false;
    for (int i = 0; i < V; i++) {
        // i is not there
        int cnt = 0;
        unordered_map<int, int> m;
        for (int j = 0; j < V; j++) {
            if (j == i) continue;
            m[j] = cnt;
            cnt++;
        }
        vector<pair<int,int>> newEdges;
        for (auto e : edges) {
            if (e.first == i || e.second == i) continue;
            else newEdges.push_back({m[e.first], m[e.second]});
        }
        bool isIG = isInteresting(V - 1, newEdges.size(), newEdges);
        if (isIG) {
            valid = true;
            break;
        }
    }
    return valid;
}

int main() {
    char inputFile[20] = "v8/IGv8.txt";

    #ifndef ONLINE_JUDGE
    // For getting input from input.txt file
    freopen(inputFile, "r", stdin);
    // Printing the Output to output.txt file
    freopen("output.txt", "w", stdout);
    #endif

    int cnt;
    cin >> cnt;

    int IG = 0;

    for (int i = 0; i < cnt; i++) {
        int V, E;
        cin >> V >> E;
        vector<pair<int, int>> edges;
        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            edges.push_back({u, v});
        }
        if (!allSubgraph(V, E, edges)) {
            // H6 is not interesting and there is a H5 which is interesting
            cout << "Yeah, there is IG7 which has no VI IG6" << endl;
            cout << V << " " << E << endl;
            for (auto e : edges) cout << e.first << " " << e.second << endl;
            cout << endl;
            IG++;
        } 

        cout << endl;
    }

    cout << IG << endl;
}