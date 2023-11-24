#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<int, int> bfs (vector<vector<int>> arr, int start) {
    vector<int> a {start};
    map<int, int> b;
    b[start] = 0;
    for (int i = 0; i < a.size(); ++i) {
        for (auto x : arr[a[i]]) {
            if (find(a.begin(), a.end(), x) == a.end()) {
                a.push_back(x);
                b[x] = b[a[i]] + 1;
            }
        }
    }
    return b;
}

int main () {
    vector<vector<int>> arr;
    arr = {{},
        {2, 3, 4},
        {1},
        {1, 7, 8},
        {1, 5, 6},
        {4},
        {4, 8},
        {3, 8},
        {3, 6, 7}};


    map<int, int> mp;
    mp = bfs(arr, 1);

    for (int i = 1; i < arr.size(); ++i) cout << i << ": " << mp[i] << endl;
}