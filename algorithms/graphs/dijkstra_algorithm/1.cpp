#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

vector<int> dijkstra_algorithm (vector<vector<int>> matrix, int start) {
    vector<int> a (matrix.size(), numeric_limits<int>::max());
    a[start - 1] = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            if (matrix[i][j] < 0) continue;
            a[j] = min(a[j], a[i] + matrix[i][j]);
        }
    }
    return a;
}

int main () {
    vector<vector<int>> matrix;
    matrix = {{-1, 2, 1, -1, -1, -1},
                {2, -1, 1, 4, 5, -1},
                {1, 1, -1, 4, 6, -1},
                {-1, 4, 4, -1, 2, 6},
                {-1, 5, 6, 2, -1, 3},
                {-1, -1, -1, 6, 3, -1}};
    for (auto x : dijkstra_algorithm(matrix, 1)) cout << x << ' ';
    cout << endl;
}