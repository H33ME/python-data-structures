# --- Arrays and Matrices ---
class MyArray:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    def access(self, index):
        return self.data[index] if 0 <= index < len(self.data) else None


# --- Stack using Array ---
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None


# --- Queue using Array ---
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None


# --- Singly Linked List ---
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def delete_front(self):
        if self.head:
            self.head = self.head.next

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print("None")
