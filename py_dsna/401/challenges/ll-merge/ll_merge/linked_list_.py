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


class LinkedList:
    def __init__(self):
        """
        Instantiate and manage a singly-linked list.
        
        Initializes an empty list with head value = "None".
        """
        self.head = None

    def type_error_check(self, next_node):
        """
        Error check raises TypeError for non-type-correct data passed for next_node.
        """
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("The value passed for next_node is not a valid instance of the Node class.")

    def insert(self, value):
        """
        Insert a new node as the (new) head of a linked list.
        """
        try:
            self.head = Node(value, self.head)
            return self.head
        except:
            return "Error when attempting to use insert method."

    def includes(self, value):
        """
        Traverse a linked list to find whether the given value exists in the list.
        """
        current = self.head

        try:
            while current:
                if current.value == value:
                    return True 
                current = current.next_node
            return False
        except:
            return "Error occurred when attempting includes method."

    def append(self, value):
        """
        Append a new node with the given value to the end of a linked list.
        """
        new_node = Node(value)
        try:
            if self.head:
                current = self.head
                while current.next_node:
                    current = current.next_node
                current.next_node = new_node
            else:
                self.head = new_node
            return new_node
        except:
            return "Error occurred while attempting to append method."

    def insert_before(self, value, new_val):
        """
        Append a new node with the value new_val immediately before the node containing the first given value within a linked list.
        """
        previous = current = self.head

        try:
            while current:
                if value == current.value:
                    new_node = Node(new_val)
                    if current == self.head:
                        new_node.next_node = self.head
                        self.head = new_node
                        return new_node
                    else:
                        previous.next_node = new_node
                        new_node.next_node = current
                        return new_node
                else:
                    previous = current
                    current = current.next_node
            else:
                return -1
        except:
            return "Error occurred while attempting to insert_before method."

    def insert_after(self, value, new_val):
        """Insert a new node with the value new_val immediately after the node with the first given value.
        """
        current = self.head

        try:
            while current:
                if current.value == value:
                    new_node = Node(new_val)
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    return new_node
                else:
                    current = current.next_node
            else:
                return -1
        except:
            return "Error occurred while attempting insert_after method."

    def list_length_finder(self):
        """
        Return the count of nodes in a linked list.
        """
        node_count = 0
        current = self.head

        while current:
            node_count += 1
            current = current.next_node
        return node_count

    def value_at_kth_from_end(self, k_val):
        """
        Return the value of the node that is k from the end of a linked list.
        """
        if type(k_val) is not int:
            raise TypeError("Value supplied for k must be a positive integer.")
        if k_val >= 0:
            current = self.head
            length = self.list_length_finder()
            target = length - k_val
            
            if target < 1:
                raise ValueError("Value for k must be less that list length.")
            for _ in range(1, target):
                current = current.next_node
            return current.value
        else:
            raise ValueError("Value supplied for k must be a positive integer.")

    
    def __str__(self):
        """
        Returns a string representing all the values in the Linked List, formatted as:
        # "{ a } -> { b } -> { c } -> None
        """
        response = ""

        current = self.head

        try:
            while current:
                response += f"{{ {str(current.value)} }} -> " 
                current = current.next_node
            return response + "None"
        except:
            return "Error occurred while attempting to represent all values found in the linked list via the __str__ method."

    def __repr__(self):
        return f"LinkedList : {self.head}"
