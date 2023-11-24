#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binary_search (vector<int> arr, int key) {
    int x = arr.size() / 2;
    int i = x;
    while (arr[i] != key) {
        x /= 2;
        if (arr[i] > key) {
            i -= max(x, 1);
        } else {
            i += max(x, 1);
        }
    }
    return i;
}

int main () {
    vector<int> arr{1, -1, 3, 9, 0, 0, 4, 2, -5};
    sort(arr.begin(), arr.end());
    for (auto x : arr) cout << x << ' ';
    cout << endl;
    int x = 9;
    cout << binary_search(arr, x) << endl;
}
