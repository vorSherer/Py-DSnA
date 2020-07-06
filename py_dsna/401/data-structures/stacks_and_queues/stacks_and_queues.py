# class InvalidOperationError:
#     pass


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
        if self.top == None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return self.top

    def peek(self):
        if self.is_empty() is False:
            return self.top.value

    def pop(self):
        if self.is_empty() is False:
            stack_pop = self.top
            self.top = self.top.next
            stack_pop.next = None
            return stack_pop.value

    def __str__(self):
        stack_top_val = self.top.value if self.top else None
        return f"Stack class; top = {stack_top_val}."

    def __repr__(self):
        return f"<Stack> class; top={self.top}, current value={self.top.value}."


class Queue:
    """
    Instantiate an empty queue, with the front and rear defaulted to None, then modify the queue with Nodes.
    """
    def __init__(self):
        self._rear = None
        self._front = None

    def is_empty(self):
        return self._front == None
        # if self._front == None:
        #     return True
        # else:
        #     return False

    def enqueue(self, value):
        new_node = Node(value)
        print("1: ", self._rear)  # REMOVE
        if self._rear:
            print("2: ", self._rear.value)  # REMOVE
            self._rear.next = new_node
            self._rear = new_node
            print("3: ", self._rear.value)  # REMOVE
            print("4: ", self._front.value)  # REMOVE

        else:
            print("5: no rear here ")  # REMOVE
            self._rear = self._front = new_node
            print("6: ", self._rear.value)  # REMOVE

    def peek(self):
        if self.is_empty is False:
            return self._front.value
        
    def dequeue(self):
        if self.is_empty is False:
            from_queue = self._front
            self._front = self._front.next
            from_queue.next = None
            return from_queue.value





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
    expected = "red"
    assert actual == expected