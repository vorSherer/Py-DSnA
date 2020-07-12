class Node:
    """
    Instantiate a node containing the given value and pointing to the given next node (defaulting to None).
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    # def __str__(self):
    #     next_val = self.next.value if self.next else None
    #     return f"Node value = {self.value} and next node = {next_val}."

    # def __repr__(self):
    #     next_val = self.next.value if self.next else None
    #     return f"<Node> class; value={self.value}, next={next_val}"


class Stack:
    """
    Instantiate an empty stack with top defaulted to None, then build the stack using Nodes.
    """
    def __init__(self):
        self.top = None
        
    # def is_empty(self):
    #     """
    #     Return True if the stack is empty.
    #     """
    #     if self.top == None:
    #         return True
    #     else:
    #         return False

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


class PseudoQueue:
    """
    Instantiate a queue-like implementation using two stacks internally. Stacks have only push, pop, and peek methods available, and the class has enqueue and dequeue methods available.
    """
    def __init__(self):
        self._front = Stack()
        self._rear = Stack()

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass





if __name__ == "__main__":
    pass
