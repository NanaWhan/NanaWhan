class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

class Queue:
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

class LinkedList:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def prepend(self, data):
        self.head = self.Node(data, self.head)
        self._size += 1
    
    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.Node(data)
        self._size += 1
    
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def size(self):
        return self._size
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

if __name__ == "__main__":
    s = Stack()
    for i in range(5):
        s.push(i)
    print(f"Stack: {[s.pop() for _ in range(s.size())]}")
    
    ll = LinkedList()
    for x in ["a", "b", "c"]:
        ll.append(x)
    print(f"LinkedList: {ll.to_list()}")
