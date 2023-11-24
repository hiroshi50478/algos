class Node:
    def __init__(self, data, link=0):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self, *data):
        self.data = len(data)
        self.link = Node(data[-1])
        for i in range(len(data) - 2, -1, -1):
            self.link = Node(data[i], self.link)
    
    def get(self):
        a = []
        node = self.link
        while node.link != 0:
            a += [node.data]
            node = node.link
        a += [node.data]
        
        return a

    def get_obj(self, index):
        node = self.link
        for _ in range(index):
            node = node.link
        
        return node

    def add(self, index, *data):
        node_start = self.get_obj(index - 1)
        if index < self.data:
            node_end = self.get_obj(index)
            node = Node(data[-1], node_end)
            for i in range(len(data) - 2, -1, -1):
                node = Node(data[i], node)
            node_start.link = node

    def delete(self, index_start, index_end=None):
        if index_end == None:
            index_end = index_start
        

a = LinkedList(1,23, 4551, 1)
print(a.get())
print(a.get_obj(2).data)
a.add(1, 5, 1231, 19, 5, 92, 12)
print(a.get())