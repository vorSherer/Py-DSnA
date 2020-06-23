class Node:
    """
    Instantiate a new node for the linked list.
    """
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
    """
    Instantiate and manage a singly-linked list.
    """
    def __init__(self):
        """
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
        Inserts a new node as the (new) head of a linked list.
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
        Appends a new node with the given value to the end of a linked list.
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
        Appends a new node with the new value immediately before the node containing the first value within the linked list.
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
        """Inserts a new node with the given value immediately after the node with the first value.
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
        Returns the count of the nodes in the linked list.
        """
        node_count = 0
        current = self.head

        while current:
            node_count += 1
            current = current.next_node
        return node_count

    def value_at_kth_from_end(self, k_val):
        """
        Returns the value of the node that is k from the end of the linked list.
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

    def merge_lists(self, list1, list2):
        """
        Merges two singly linked lists in place in 'zipper' fashion, alternating nodes from each of the given lists into the first list and vacating the second.
        """
        try:
            if list1.self.head.next_node == None:
                list1.self.head = list2.self.head
                list2.self.head == None
            
            list1_current_node = list1.self.head
            list1_next_node = list1.self.head.next_node
            list2_current_node = list2.self.head
            list2_next_node = list2.self.head.next_node

            while list1.current.next_node and list2.current.next_node:
                list2.head.next_node = list1_next_node
                list1.current.next_node = list2.self.head                      
                list1.current = list1_next_node
                list2.self.head = list2_next_node
                list2_next_node = list2.self.head.next_node
                list1_next_node = list1.current.next_node
            if list2.self.head.next_node == None:
                list2.self.head.next_node = list1.current.next_node
                iist1.current.next_node = list2.self.head
            else:
                list1.current.next_node = list2.self.head
            return list1.self.head
        except:
            return "Error occurred while attempting the merge_lists method."



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



if __name__ == "__main__":
    ll = LinkedList()
    # apples = ll.insert('apples')
    # print(apples.value)
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("cantaloupes")
    ll.insert("d'Anjou pears")
    ll.insert_after("bananas", "limes")
    print(str(ll))
    # print("Head val ", ll.head.value)
    # print("Next val ", ll.head.next_node.value)
    # print(ll.value_at_kth_from_end(5))
    # print(ll.value_at_kth_from_end(-2))
    print(ll.value_at_kth_from_end("one"))
