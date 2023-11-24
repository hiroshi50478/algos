#include <iostream>
#include <vector>

using namespace std;

vector<int> bubble_sort(vector<int> arr) {
    for (int i = 0; i < arr.size(); ++i) {
        for (int j = 0; j < arr.size() - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                int x = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = x;
            }
        }
    }
    
    return arr;
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = bubble_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
