#include <iostream>

using namespace std;


class Stack {
private:
	int index;
	int length;
	int* data;
public:
	Stack(int _length);
	~Stack();
	void push(int value);
	int pop();
};

Stack::Stack(int _length) {
	index = 0;
	length = _length;
	data = (int*)malloc(sizeof(int) * length);
}

Stack::~Stack() {
	free(data);
}

void Stack::push(int value) {
	data[index] = value;
	++index;
}

int Stack::pop() {
	--index;
	return data[index];
}


int main() {
	Stack stack = Stack(5);

	stack.push(123);
	stack.push(12);
	stack.push(1);

	cout << stack.pop() << endl;
	cout << stack.pop() << endl;
	cout << stack.pop() << endl;

	return 0;
}
