# Stacks and Queues
<!-- Short summary or background information -->

## Challenge
#### Features
- Create a __`Node`__ class that has properties for the __value__ stored in the Node, and a pointer to the __next node__.
- Create a __`Stack`__ class that has a __top__ property. It creates an empty Stack when instantiated.
    - This object should be aware of a default empty value assigned to top when the stack is created.
    - Define a method called __`push`__ which takes any __value__ as an argument and adds a __new node__ with that value to the __top__ of the stack with an __*O(1) Time*__ performance.
    - Define a method called __`pop`__ that *does not* take any argument, __removes__ the node from the top of the stack, and __returns the node’s value__.
        - Should raise exception when called on empty stack
    - Define a method called __`peek`__ that *does not* take an argument and __returns the value of the node located on top__ of the stack, without removing it from the stack.
        - Should raise exception when called on empty stack
    - Define a method called __`isEmpty`__ that takes *no argument*, and __returns a boolean__ indicating whether or not the stack is empty. <br>

- Create a __`Queue`__ class that has a __`front`__ property. It creates an empty Queue when instantiated.
    - This object should be aware of a default empty value assigned to front when the queue is created.
    - Define a method called __`enqueue`__ which takes any __value__ as an argument and adds a __new node__ with that value to the back of the queue with an __*O(1) Time*__ performance.
    - Define a method called __`dequeue`__ that *does not* take any argument, __removes the node from the front__ of the queue, and __returns the node’s value__.
        - Should raise exception when called on empty queue
    - Define a method called __`peek`__ that *does not* take an argument and __returns the value of the node located in the front__ of the queue, __*without removing it from the queue*__.
        - Should raise exception when called on empty queue
    - Define a method called __`isEmpty`__ that takes *no argument*, and __returns a boolean__ indicating whether or not the queue is empty. <br>

- Be sure to follow your languages best practices for naming conventions.
- You have access to the __`Node`__ class and all the properties on the __`Linked List`__ class.

## Approach & Efficiency
Both Stack and Queue were implemented using a singly linked list methodology. <br>
__Big O space__ for each will be __O(n)__ and <br>
__Big O time__ for each operation is __O(1)__.

## API
<!-- Description of each method publicly available to your Stack and Queue-->

<!-- ## Code Challenge 10 whiteboards:
![CC-10 Stack -1](./assets/stack_WB-1.png)
![CC-10 Queue -1](./assets/queue_WB-1.png)
 -->

## Task Checklist: <br>
- [ ] Top-level README “Table of Contents” is updated <br>
- [  Feature tasks for this challenge are completed <br>
- [ ] Unit tests written and passing <br>
    - [ ] “Happy Path” - Expected outcome <br>
    - [ ] Expected failure <br>
    - [ ] Edge Case (if applicable/obvious) <br>
- [ ] README for this challenge is complete <br>
    - [ ] Summary, Description, Approach & Efficiency, Solution <br>
    - [ ] Link to code <br>
    - [ ] Pictures of whiteboards <br>
