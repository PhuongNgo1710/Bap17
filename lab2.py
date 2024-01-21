

class EmptyStackException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def isEmpty(self):
        return self.top_node is None

    def clear(self):
        self.top_node = None

    def push(self, x):
        new_node = StackNode(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.top_node.data

    def traverse(self):
        current = self.top_node
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def decimal_to_binary(decimal_number):
    binary_stack = Stack()

    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_stack.push(remainder)
        decimal_number //= 2

    binary_result = ''
    while not binary_stack.isEmpty():
        binary_result += str(binary_stack.pop())

    return binary_result

if __name__ == "__main__":
    stack_example = Stack()

    # Pushing elements onto the stack
    stack_example.push(5)
    stack_example.push(10)
    stack_example.push(15)

    # Displaying the stack
    print("Traversing the stack:")
    stack_example.traverse()

    # Converting an integer from decimal to binary using the stack
    decimal_number = 42
    binary_result = decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number}: {binary_result}")
#Question 2:

class EmptyQueueException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new_node = QueueNode(x)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def first(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.front.data

    def traverse(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def decimal_to_binary_fraction(decimal_fraction):
    binary_queue = Queue()
    precision = 10  # You can adjust the precision as needed

    while decimal_fraction > 0 and precision > 0:
        decimal_fraction *= 2
        bit = int(decimal_fraction)
        binary_queue.enqueue(bit)
        decimal_fraction -= bit
        precision -= 1

    binary_result = ''
    while not binary_queue.isEmpty():
        binary_result += str(binary_queue.dequeue())

    return binary_result

if __name__ == "__main__":
    queue_example = Queue()

    # Enqueuing elements onto the queue
    queue_example.enqueue(5)
    queue_example.enqueue(10)
    queue_example.enqueue(15)

    # Displaying the queue
    print("Traversing the queue:")
    queue_example.traverse()

    # Converting a real number less than 1 to binary using the queue
    decimal_fraction = 0.375
    binary_result = decimal_to_binary_fraction(decimal_fraction)
    print(f"Binary representation of {decimal_fraction}: 0.{binary_result}")
#Question 3:

class EmptyStackException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def isEmpty(self):
        return self.top_node is None

    def clear(self):
        self.top_node = None

    def push(self, x):
        new_node = StackNode(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.top_node.data

    def traverse(self):
        current = self.top_node
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main_stack_test():
    stack_example = Stack()
    stack_example.push("Apple")
    stack_example.push("Banana")
    stack_example.push("Cherry")

    print("Traversing the stack:")
    stack_example.traverse()

    print("Top of the stack:", stack_example.top())

    popped_value = stack_example.pop()
    print("Popped value:", popped_value)
    print("Is the stack empty?", stack_example.isEmpty())

    stack_example.clear()
    print("Is the stack empty after clear?", stack_example.isEmpty())

# 2. Modified Queue Implementation:

class EmptyQueueException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new_node = QueueNode(x)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def first(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.front.data

    def traverse(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main_queue_test():
    queue_example = Queue()
    queue_example.enqueue("Dog")
    queue_example.enqueue("Cat")
    queue_example.enqueue("Fish")

    print("Traversing the queue:")
    queue_example.traverse()

    print("First element of the queue:", queue_example.first())

    print("Dequeue operation result:", queue_example.dequeue())
    print("Is the queue empty?", queue_example.isEmpty())

    print("Clearing the queue.")
    queue_example.clear()
    print("Is the queue empty after clear?", queue_example.isEmpty())

if __name__ == "__main__":
    print("Testing Stack:")
    main_stack_test()

    print("\nTesting Queue:")
    main_queue_test()
#Question 4:

class EmptyStackException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def isEmpty(self):
        return self.top_node is None

    def clear(self):
        self.top_node = None

    def push(self, x):
        new_node = StackNode(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.top_node.data

    def traverse(self):
        current = self.top_node
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main_stack_test():
    stack_example = Stack()
    stack_example.push('A')
    stack_example.push('B')
    stack_example.push('C')

    print("Traversing the stack:")
    stack_example.traverse()

    print("Top of the stack:", stack_example.top())

    popped_value = stack_example.pop()
    print("Popped value:", popped_value)
    print("Is the stack empty?", stack_example.isEmpty())

    stack_example.clear()
    print("Is the stack empty after clear?", stack_example.isEmpty())

# 2. Modified Queue Implementation:

class EmptyQueueException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new_node = QueueNode(x)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def first(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.front.data

    def traverse(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

def main_queue_test():
    queue_example = Queue()
    queue_example.enqueue('X')
    queue_example.enqueue('Y')
    queue_example.enqueue('Z')

    print("Traversing the queue:")
    queue_example.traverse()

    print("First element of the queue:", queue_example.first())

    print("Dequeue operation result:", queue_example.dequeue())
    print("Is the queue empty?", queue_example.isEmpty())

    print("Clearing the queue.")
    queue_example.clear()
    print("Is the queue empty after clear?", queue_example.isEmpty())

if __name__ == "__main__":
    print("Testing Stack:")
    main_stack_test()

    print("\nTesting Queue:")
    main_queue_test()
#Question 5:

class EmptyStackException(Exception):
    pass

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def isEmpty(self):
        return self.top_node is None

    def clear(self):
        self.top_node = None

    def push(self, x):
        new_node = StackNode(x)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        data = self.top_node.data
        self.top_node = self.top_node.next
        return data

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.top_node.data

    def traverse(self):
        current = self.top_node
        while current:
            print(current.data.name, end=' ')
            current = current.next
        print()

class Computer:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

def main_stack_test():
    stack_example = Stack()
    stack_example.push(Computer("Desktop1", "Dell"))
    stack_example.push(Computer("Laptop1", "HP"))
    stack_example.push(Computer("Server1", "Lenovo"))

    print("Traversing the stack:")
    stack_example.traverse()

    print("Top of the stack:", stack_example.top().name)

    popped_value = stack_example.pop()
    print("Popped value:", popped_value.name)
    print("Is the stack empty?", stack_example.isEmpty())

    stack_example.clear()
    print("Is the stack empty after clear?", stack_example.isEmpty())

# 2. Modified Queue Implementation:

class EmptyQueueException(Exception):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def clear(self):
        self.front = self.rear = None

    def enqueue(self, x):
        new_node = QueueNode(x)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def first(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.front.data

    def traverse(self):
        current = self.front
        while current:
            print(current.data.name, end=' ')
            current = current.next
        print()

def main_queue_test():
    queue_example = Queue()
    queue_example.enqueue(Computer("Desktop2", "Acer"))
    queue_example.enqueue(Computer("Laptop2", "Lenovo"))
    queue_example.enqueue(Computer("Server2", "Dell"))

    print("Traversing the queue:")
    queue_example.traverse()

    print("First element of the queue:", queue_example.first().name)

    print("Dequeue operation result:", queue_example.dequeue().name)
    print("Is the queue empty?", queue_example.isEmpty())

    print("Clearing the queue.")
    queue_example.clear()
    print("Is the queue empty after clear?", queue_example.isEmpty())

if __name__ == "__main__":
    print("Testing Stack:")
    main_stack_test()

    print("\nTesting Queue:")
    main_queue_test()