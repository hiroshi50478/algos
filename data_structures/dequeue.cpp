#include <iostream>

using namespace std;


class Dequeue {
private:
	int index_begin;
	int index_end;
	int length;
	int* data;
public:
	Dequeue(int _length);
	~Dequeue();
	void push_begin(int value);
	int pop_begin();
	void push_end(int value);
	int pop_end();
};

Dequeue::Dequeue(int _length) {
	index_begin = (_length - 1) / 2;
	index_end = index_begin + 1;
	length = _length;
	data = (int*)malloc(sizeof(int) * length);
}

Dequeue::~Dequeue() {
	free(data);
}

void Dequeue::push_begin(int value) {
	data[index_begin] = value;
	--index_begin;
	if (index_begin == -1) {
		index_begin = length - 1;
	}
}

int Dequeue::pop_begin() {
	++index_begin;
	if (index_begin == length) {
		index_begin = 0;
	}
	return data[index_begin];
}

void Dequeue::push_end(int value) {
	data[index_end] = value;
	++index_end;
	if (index_end == length) {
		index_end = 0;
	}
}

int Dequeue::pop_end() {
	--index_end;
	if (index_end == -1) {
		index_end = length - 1;
	}
	return data[index_end];
}


int main() {
	Dequeue dequeue = Dequeue(7);

	dequeue.push_end(1);
	dequeue.push_end(2);
	dequeue.push_end(3);
	dequeue.push_end(5);
	dequeue.push_end(6);
	dequeue.push_begin(7);	

	cout << dequeue.pop_end() << endl;
	cout << dequeue.pop_end() << endl;
	cout << dequeue.pop_end() << endl;
	cout << dequeue.pop_end() << endl;
	cout << dequeue.pop_end() << endl;

	cout << dequeue.pop_begin() << endl;

	return 0;
}
