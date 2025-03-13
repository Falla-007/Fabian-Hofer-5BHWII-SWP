import random

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

if __name__ == "__main__":
    ll = LinkedList()
    for _ in range(10):  # Füge 10 zufällige Werte hinzu
        ll.append(random.randint(1, 100))
    
    print("Länge der Liste:", len(ll))
    print("Elemente der Liste:")
    ll.display()
    
    print("Iteriere über die Liste:")
    for value in ll:
        print(value, end=" ")
