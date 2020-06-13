class LinkedList:
# ***************************************
# Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

    def __init__(self):   #, value=None):
        # self.value = value
        self.head = None

    def __repr__(self):
        return f"LinkedList : {self.head}"

# ***************************************
# Define a method called __str__ which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
# ****************************************

    def __str__(self):
        '''
        { bananas } --> { apples } --> NULL
        '''
        response = ""

        current = self.head

        while current:
            response += f"{{ {str(current.value)} }} -> " 
            current = current.next_node

        return response + "NULL"

# ***************************************
# Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.

    def insert(self, value):

        self.head = Node(value, self.head)


# ***************************************
# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True 
            current = current.next_node
        return False


# ***************************************
# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.


class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def has_value(self):
        return self.value

    def get_next(self):
        return self.next_node


#     # To throw an exception deliberately - test_insert_empty...
#     # research a better way to write this, would usually do "Duck Typing":
#     # if not isinstance(next_, Node) and next_ != None:
#     #   raise TypeError("Next node 

    def __repr__(self):
        return f"{self.value} : {self.next}"

# if __name__ == "__main__":
    
#     apples = Node("apples")

#     bananas = Node("bananas")

#     apples.next = bananas

#     print(apples)


    # fruit = LinkedList()

    # fruit.head = apples

    # print(fruit)

