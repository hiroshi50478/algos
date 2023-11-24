#include <iostream>
#include <vector>

using namespace std;

vector<int> selection_sort(vector<int> arr) {
    for(int i = 0; i < int(arr.size()) - 1; ++i) {
        int _i = i;
        for (int j = i + 1; j < arr.size(); ++j) {
            if (arr[j] < arr[_i]) _i = j;
        }
        swap(arr[i], arr[_i]);
    }

    return arr;
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = selection_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
