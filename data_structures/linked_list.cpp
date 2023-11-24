#include <iostream>

using namespace std;


typedef struct Node {
	Node* next;
	int value;
} Node;

class LinkedList {
public:
	LinkedList();
	~LinkedList();
	void push(int index, int value);
	int get(int index);
	void pop(int index);
	void print();
private:
	Node* head;
	int length;
};

LinkedList::LinkedList() {
	head = NULL;
	length = 0;
}

LinkedList::~LinkedList() {
	Node* previous_node = NULL;
	Node* current_node = head;
	while (current_node != NULL) {
		previous_node = current_node;
		current_node = current_node->next;
		free(previous_node);
	}
}

void LinkedList::push(int index, int value) {
	if (index == 0) {
		Node* new_node = (Node*)malloc(sizeof(Node));
		new_node->next = head;
		new_node->value = value;
		head = new_node;
	} else {
		int current_index = 0;
		Node* previous_node = head;
		while (current_index < index - 1) {
			++current_index;
			previous_node = previous_node->next;
		}
		Node* new_node = (Node*)malloc(sizeof(Node));
		previous_node->next = new_node;
		new_node->next = previous_node->next;
		new_node->value = value;
	}
	++length;
}

int LinkedList::get(int index) {
	int current_index = 0;
	Node* current_node = head;
	while (current_index < index) {
		++current_index;
		current_node = current_node->next;
	}
	return current_node->value;
}

void LinkedList::pop(int index) {
	int current_index = 0;
	Node* previous_node = NULL;
	Node* current_node = head;
	while (current_index < index) {
		++current_index;
		previous_node = current_node;
		current_node = current_node->next;
	}
	
	if (previous_node != NULL) {
		previous_node->next = current_node->next;
	}
	
	free(current_node);
	--length;
}

void LinkedList::print() {
	Node* current_node = head;
	for (int i = 0; i < length; ++i) {
		cout << current_node->value << ' ';
		current_node = current_node->next;
	}
	cout << endl;
}


int main() {
	LinkedList list;

	list.push(0, 123);
	list.push(1, 12);
	list.push(2, 1);

	list.print();
	list.pop(0);
	list.print();
	list.pop(0);
	list.print();
	list.pop(0);

	return 0;
}