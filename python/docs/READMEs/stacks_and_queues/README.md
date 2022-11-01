# Stacks and Queues
Stack is implemented as a singly linked list with a "top" reference to the head of the linked list.\
Queue is implemented as a singly linked list with a "front" reference to the head of the linked list and a "rear"
reference to the tail of the linked list.

## Challenge
Implement a Stack class and a Queue class with methods detailed below. Handle case of empty stack/queue when
appropriate.

## Approach & Efficiency
All Stack and Queue methods detailed below run in constant time, O(1). This is because direct references allow
constant time access to the top of a stack, and to both the front and rear of a queue.

## API
Stack Methods:
- push: takes a value as an argument, creates a node with that value, adds it to the top of the stack
- pop: removes the top node from the stack and returns its value
- peek: returns the top node's value
- is_empty: returns True if stack is empty, otherwise returns False

Queue Methods:
- enqueue: takes a value as an argument, creates a node with that value, adds it to the rear of the queue
- dequeue: removes the front node from the queue and returns its value
- peek: returns the front node's value
- is_empty: returns True if queue is empty, otherwise returns False
