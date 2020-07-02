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
    Instantiate an empty stack with top defaulted to None.
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

    def pop(self):
        if is_empty() is False:
            stack_pop = self.top
            self.top = top.next_
            stack_pop.next = None
            return stack_pop.value

    def peek(self):
        if is_empty()is False:
            return self.top.value

    def __str__(self):
        return f"Stack class; top = {self.top} with current value = {self.top.value}."

    def __repr__(self):
        return f"<Stack> class; top={self.top}, current value={self.top.value}."




if __name__ == "__main__":
    new_node = Node("apples")
    print(new_node)
