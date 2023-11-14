#include <iostream>

using namespace std;


void print(int* data, int length) {
	for (int i = 0; i < length; ++i) {
		cout << data[i] << ' ';
	}
	cout << endl;
}

void insertion_sort(int* data, int length) {
	for (int i = 1; i < length; ++i) {
		for (int j = i; (j > 0) && (data[j - 1] > data[j]); --j) {
			swap(data[j - 1], data[j]);
		}
	}
}


int main() {
	int data[] = {3, 0, -12, 45, 2, 75, 3, 9, 12, -33};
	int length = sizeof(data) / sizeof(int);

	print(data, length);
	insertion_sort(data, length);
	print(data, length);

	return 0;
}
