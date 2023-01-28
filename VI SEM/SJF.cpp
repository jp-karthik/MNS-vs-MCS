#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <string>
#include <queue>
#include <set>

using namespace std;

class Process {
public:
    
    int PID = -1;
    int arrivalTime = -1;
    int responseTime = -1;
    int turnAroundTime = -1;
    bool finished = false;
    deque<pair<int,char>> info;
    
    Process(vector<int>& tokens, int PID) {
        this->PID = PID;
        this->arrivalTime = tokens[0];
        bool IO = false;
        for (int i = 1; i < tokens.size(); i++) {
            if (IO) info.push_back({tokens[i], 'I'});
            else info.push_back({tokens[i], 'C'});
            IO = !IO;
        }
    }
    
};

vector<Process*> processList;
set<pair<pair<int,int>,Process*>> readyQ;
queue<Process*> blockedQ;

int counter = 0;
int IDX = 0;

void getAvailableProcesses() {
    for (; IDX < processList.size(); IDX++) {
        if (processList[IDX]->arrivalTime <= counter) {
            int burstTime = processList[IDX]->info[0].first;
            int arrivalTime = processList[IDX]->arrivalTime;
            readyQ.insert({{burstTime, arrivalTime}, processList[IDX]});
        } else break;
    }
}

void runIO() {
    if (blockedQ.size()) {
        Process* front = blockedQ.front();
        front->info[0].first--;
        if (front->info[0].first == 0) {
            blockedQ.pop();
            front->info.pop_front();
            if (front->info.size()>0) {
                int burstTime = front->info[0].first;
                int arrivalTime = front->arrivalTime;
                readyQ.insert({{burstTime, arrivalTime}, front});
            } else {
                front->finished = true;
                front->turnAroundTime = counter - front->arrivalTime + 1;
            }
        }
    }
}

void runCPU() {
    if (readyQ.size()) {
        pair<pair<int,int>,Process*> top = *readyQ.begin();
        readyQ.erase(readyQ.begin());
        if (top.second->responseTime == -1) {
            top.second->responseTime = counter - top.second->arrivalTime;
        }
        int burstTime = top.first.first;
        for (int i = 0; i < burstTime; i++) {
            runIO();
        }
        top.second->info.pop_front();
        if (top.second->info.size()>0) {
            blockedQ.push(top.second);
        } else {
            top.second->finished = true;
            top.second->turnAroundTime = counter + burstTime - top.second->arrivalTime;
        }
        counter += burstTime;
    }
}

int main(int argc, char* argv[]) {
    
    ifstream OSin;
    ofstream OSout;
    OSin.open(argv[1]); 
    OSout.open("SJF.txt");

    int PID = 0;
    while (OSin.eof()==false) {
        string s;
        getline(OSin, s);
        vector<int> tokens;
        string temp = "";
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ') {
                tokens.push_back(stoi(temp));
                temp.clear();
            } else {
                temp += s[i];
            }
        }
        Process* process = new Process(tokens, PID);
        processList.push_back(process);
        PID += 1;
    }

    while(IDX!=processList.size() || readyQ.size()>0 || blockedQ.size()>0) {
        getAvailableProcesses();
        if (readyQ.size()>0) runCPU();
        else {
            runIO();
            counter++;
        }
    }

    int cnt = 0;
    double avgRT = 0;
    double avgTAT = 0;
    for (int i = 0; i < processList.size(); i++) {
        if (processList[i]->finished) {
            cnt++;
            OSout << processList[i]->responseTime << " " << processList[i]->turnAroundTime << endl;
            avgRT += processList[i]->responseTime;
            avgTAT += processList[i]->turnAroundTime;
        }
    }
    avgRT /= (double) processList.size();
    avgTAT /= (double) processList.size();
    
    OSout << "#processes: " << cnt << endl;
    OSout << "#avgRT: " << avgRT << endl;
    OSout << "#avgTAT: " << avgTAT << endl;

    OSout.close();
    OSin.close();

    return 0;
}