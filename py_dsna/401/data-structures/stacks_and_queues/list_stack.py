class Stack:
    """
    Instantiate a stack using a Python List.
    """
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        else:
            return "stack is empty"
    
    def is_empty(self):
        return not len(self.storage)
        # if len(self.storage) == 0:
        #   return True
        # return False
    
    def peek(self):
        if not self.is_empty():
            return self.storage[-1]
        else:
            return "stack is empty"
