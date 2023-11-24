#include <iostream>
#include <vector>

using namespace std;

vector<int> binary_sort(vector<int> arr) {
    if (arr.size() <= 1) {
        return arr;
    } else {
        vector<int> left, right;
        int mid = arr.size() / 2;
        for (int i = 0; i < arr.size(); ++i) {
            if (i != mid) {
                if (arr[i] <= arr[mid]) {
                    left.push_back(arr[i]);
                } else {
                    right.push_back(arr[i]);
                }
            }
        }
        left = binary_sort(left);
        right = binary_sort(right);

        left.push_back(arr[mid]);
        left.insert(left.end(), right.begin(), right.end());
        
        return left;
    }
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = binary_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
