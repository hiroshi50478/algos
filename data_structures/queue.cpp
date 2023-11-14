#include <iostream>

using namespace std;


class Queue {
private:
	int index_begin;
	int index_end;
	int length;
	int* data;
public:
	Queue(int _length);
	~Queue();
	void push(int value);
	int pop();
};

Queue::Queue(int _length) {
	index_begin = 0;
	index_end = 0;
	length = _length;
	data = (int*)malloc(sizeof(int) * length);
}

Queue::~Queue() {
	free(data);
}

void Queue::push(int value) {
	data[index_end] = value;
	++index_end;
	if (index_end == length) {
		index_end = 0;
	}
}

int Queue::pop() {
	++index_begin;
	if (index_begin == length) {
		index_begin = 0;
		return data[length - 1];
	} else {
		return data[index_begin - 1];
	}
}


int main() {
	Queue queue = Queue(5);

	queue.push(123);
	queue.push(12);
	queue.push(1);
	queue.push(5);
	queue.push(4);

	cout << queue.pop() << endl;
	cout << queue.pop() << endl;
	cout << queue.pop() << endl;

	queue.push(99);
	queue.push(0);
	queue.push(13);

	cout << queue.pop() << endl;
	cout << queue.pop() << endl;
	cout << queue.pop() << endl;
	cout << queue.pop() << endl;
	cout << queue.pop() << endl;

	return 0;
}
