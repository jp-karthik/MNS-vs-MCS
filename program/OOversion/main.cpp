// header files
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include "MNS.cpp"
#include "MCS.cpp"
using namespace std;

int getMinIdxOfProblem(MNS* mns, MCS* mcs) {
    int mn = 10;
    for (auto MNSorder : mns->MNS_orderings) {
        int val = 0;
        for (auto MCSorder : mcs->MCS_orderings) {
            if (MCSorder == MNSorder) {
                val = 10;
                continue;
            }
            int cnt = 0;
            for (int i = 0; i < MNSorder.size() && MCSorder.size(); i++) {
                if (MNSorder[i] == MCSorder[i]) {
                    cnt++;
                } else {
                    cnt++;
                    break;
                }
            }
            val = max(val, cnt);
        }
        mn = min(mn, val);
    }
    return mn;
}
bool isInteresting(int V, int E, vector<pair<int,int>>& edges) {
    MNS* mns = new MNS(V, E, edges);
    MCS* mcs = new MCS(V, E, edges);

    mns->performAllPossible();
    mcs->performAllPossible();
    
    int mnsSize = mns->getSize();
    int mcsSize = mcs->getSize();
    
    if (mnsSize == mcsSize) {
        return false;
    } else {
        if (getMinIdxOfProblem(mns, mcs) == 5) {
            cout << 5 << endl;
            cout << V << " " << E << endl;
            for (auto e : edges) cout << e.first << " " << e.second << endl;
            cout << endl;
        }
    }

    delete mns;
    delete mcs;
    if (mnsSize == mcsSize) return false;
    else return true;
}

int main() {
    char inputFile[20] = "v6/IGv6.txt";

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
        isInteresting(V, E, edges);

        // if (!isInteresting(V, E, edges)) {
        //     IG++;
        //     cout << V << " " << E << endl;
        //     for (auto e : edges) cout << e.first << " " << e.second << endl;
        // }
    }
    //cout << IG << endl;
}