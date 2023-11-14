#include <iostream>


using namespace std;


void print(int* data, int length) {
	for (int i = 0; i < length; ++i) {
		cout << data[i] << ' ';
	}
	cout << endl;
}


void bubble_sort(int* data, int length) {
	for (int i = 0; i < length; ++i) {
		for (int j = 0; j < length - 1 - i; ++j) {
			if (data[j] > data[j + 1]) {
				swap(data[j], data[j + 1]);
			}
		}
	}
}


int main() {
	int data[] = {3, 0, -12, 45, 2, 75, 3, 9, 12, -33};
	int length = sizeof(data) / sizeof(int);

	print(data, length);
	bubble_sort(data, length);
	print(data, length);

	return 0;
}
