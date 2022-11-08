# Pseudo-Queue

This pseudo-queue was implemented using two stacks, but behaves externally like a queue (FIFO), and supports an
enqueue and a dequeue method.

Enqueue: takes a value, adds it to the queue
Dequeue: removes the last value from the queue and returns it

## Efficiency

Values can be added in O(1) time. But removing values is O(n) time, since all values in the underlying stack must be
copied to a temporary stack, so the last element can be removed, and then the value must be copied a second time
back to the original stack.

## Whiteboard

