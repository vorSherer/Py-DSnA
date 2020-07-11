class Node:
    def __init__(self, value, next_node=None):
        """
        Instantiate a node using the given value and optional next_node data.
         
        If no value is supplied for next_node, it will be initialized to "None," indicating that this will be the head node of a new linked list.
        """
        self.type_error_check(next_node)
        self.value = value
        self.next_node = next_node

    def has_value(self):
        """
        Returns self.value for testing purposes
        """
        return self.value

    def get_next(self):
        """
        Returns self.next_node for testing purposes
        """
        return self.next_node

    def type_error_check(self, next_node):
        """
        Error check raises TypeError for non-type-correct data passed for next_node.
        """
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("The value passed for next_node is not a valid instance of the Node class.")

    def __str__(self):
        return f"{self.value} : {self.next_node}"

    def __repr__(self):
        return f"<Node> value={self.value}, next node={self.next_node}"

