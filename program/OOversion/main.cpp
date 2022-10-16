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

int main() {
    char inputFile[20] = "v6/NIGv6.txt";

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
        if (isInteresting(V, E, edges)) {
            IG++;
            cout << V << " " << E << endl;
            for (auto e : edges) cout << e.first << " " << e.second << endl;
            cout << endl;
        }

        cout << endl;
    }
    cout << IG << endl;
}