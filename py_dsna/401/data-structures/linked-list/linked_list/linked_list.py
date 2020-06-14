# Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).
# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

class Node:
    '''
    This is the Node class. It is used to instantiate a new node for the linked list.
    '''
    def __init__(self, value, next_node=None):
        '''
        This function initializes the Node class. It takes in a value and an optional value for next_node, pointing to the next node in the list. An error check will prevent non-type-correct data from being instantiated as a node. If no value is supplied for next_node, it will be initialized to "None," indicating that this will be the head node.
        '''
        self.value = value
        self.next_node = next_node

    def has_value(self):
        '''
        This method returns self.value for testing purposes
        '''
        return self.value

    def get_next(self):
        '''
        This method returns self.next_node for testing purposes
        '''
        return self.next_node


    def __repr__(self):
        return f"{self.value} : {self.next_node}"


# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
class LinkedList:
    '''
    This is the Linked List class object. It is used to instantiate and manage a singly-linked list.
    '''
    def __init__(self, value=None):
        '''
        This function initializes the Linked List class.  It takes in a value as an argument that will be passed to the Node class for instantiation, or if no value is provided, the default will be "None".
        '''
        self.value = value
        self.head = None

# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.
    def type_error_check(self, next_node):
        '''
        This error check prevents non-type-correct data from being instantiated as a node.
        '''
        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("The value passed for next_node is not a valid instance of the Node class.")
# Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
    def insert(self, value):
        '''
        This method inserts a new node as the (new) head of a linked list.
        '''
        try:
            if type_error_check(next_node):
                self.head = Node(value, self.head)
        except:
            return "Error when attempting to use insert method."


# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):

        current = self.head

        try:
            while current:
                if current.value == value:
                    return True 
                current = current.next_node
            return False
        except:
            return "Error occurred when attempting includes method."
            
# Define a method called __str__ which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
    def __str__(self):
        '''
        This method takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        # "{ a } -> { b } -> { c } -> None
        '''
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
    apples = Node('apples')
    print(apples)
