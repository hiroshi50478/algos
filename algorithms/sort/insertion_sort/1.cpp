#include <iostream>
#include <vector>

using namespace std;

vector<int> insertion_sort(vector<int> arr)
{
    for (int i = 1; i < arr.size(); ++i)
    {
        int x = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > x)
        {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = x;
    }
    return arr;
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = insertion_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
