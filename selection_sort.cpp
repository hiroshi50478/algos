#include <iostream>


using namespace std;


void print(int* data, int length) {
	for (int i = 0; i < length; ++i) {
		cout << data[i] << ' ';
	}
	cout << endl;
}


void selection_sort(int* data, int length) {
	int index_min;
	for (int i = 0; i < length; ++i) {
		index_min = i;
		for (int j = i; j < length; ++j) {
			if (data[j] < data[index_min]) {
				index_min = j;
			}
		}
		swap(data[i], data[index_min]);
	}
}


int main() {
	int data[] = {3, 0, -12, 45, 2, 75, 3, 9, 12, -33};
	int length = sizeof(data) / sizeof(int);

	print(data, length);
	selection_sort(data, length);
	print(data, length);

	return 0;
}
