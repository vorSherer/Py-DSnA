class Node:
    """
    Create a node containing the given value and pointing to the given next node (defaulting to None).
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        next_val = self.next.value if self.next else None
        return f"Node value = {self.value} and next node = {next_val}."

    def __repr__(self):
        next_val = self.next.value if self.next else None
        return f"<Node> class; value={self.value}, next={next_val}"


class Stack:
    """
    Instantiate an empty stack with top defaulted to None, then build the stack using Nodes.
    """
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        """
        Return True if the stack is empty.
        """
        if self.top == None:
            return True
        else:
            return False

    def push(self, value):
        """
        Push a new node with the given value to the top of the stack.
        """
        new_node = Node(value, self.top)
        self.top = new_node
        return self.top

    def peek(self):
        """
        Return the value of the top node in the stack without modifying the stack, or raise an error if the stack is empty.
        """
        if self.is_empty() is False:
            return self.top.value
        else:
            raise AttributeError('The stack is empty')

    def pop(self):
        """
        Pop the top node off the stack and return its value.
        """
        if self.is_empty() is False:
            stack_pop = self.top
            self.top = self.top.next
            stack_pop.next = None
            return stack_pop.value
        else:
            raise AttributeError('The stack is empty')



class Queue:
    """
    Instantiate an empty queue, with the front and rear defaulted to None, then modify the queue with Nodes.
    """
    def __init__(self):
        self._front = None
        self._rear = None

    def is_empty(self):
        """
        Return True if queue is empty.
        """
        return self._front == None

        # return self._front is None

        # return not bool(self._front)

        # if self._front:
        #     return False
        # else:
        #     return True

    def enqueue(self, value):
        """
        Add new node with the given value to the rear of the queue. If the queue was empty, the new node also becomes the front.
        """
        new_node = Node(value)
        print("1: ", self._rear)  # REMOVE
        if self._rear:
            print("2: ", self._rear.value)  # REMOVE
            self._rear.next = new_node
            self._rear = new_node
            print("3: ", self._rear.value)  # REMOVE
            print("4: ", self._front.value)  # REMOVE
        elif self._front:
            self._front.next = new_node
            self._rear = new_node
        else:
            print("5: no rear here ")  # REMOVE
            self._rear = self._front = new_node
            print("6: ", self._rear.value)  # REMOVE
            print("Enqueue complete.")  # REMOVE

    def peek(self):
        """
        Return the value of the front node in the queue without modifying the queue, or raise an error if the queue is empty.
        """
        if self._front:
            return self._front.value
        else:
            raise AttributeError('The queue is empty.')
        
    def dequeue(self):
        """Reassign front to point to the node immediately following front, remove the front node in the queue and return it's value, or raise an error if the queue is empty.
        """
        if self._front:
            from_queue = self._front
            if self._front.next == None:
                self._front = None
                self._rear = None
            else:
                self._front = self._front.next
            from_queue.next = None
            return from_queue.value
        else:
            raise AttributeError('The queue is empty.')





if __name__ == "__main__":
    # new_node = Node("apples")
    # print(new_node)
    prism = Queue()
    prism.enqueue("red")
    print("R: ", prism._front.value)
    prism.enqueue("orange")
    print("O: ", prism._rear.value)
    prism.dequeue()
    actual = prism.peek()
    print("Peek: ", actual)
    # expected = "red"
    expected = "orange"
    assert actual == expected
    print("TEST PASSED.")