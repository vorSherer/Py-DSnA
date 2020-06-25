# Merge two singly linked lists
Given two singly linked lists, merge them in place "zipper fashion" into one list.

## Challenge Description
1. Write a function called merge_lists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. 
1. Try and keep additional space down to O(1). 
1. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
Big O space for this approach is O(1) <br>
Big O time for this approach is O(n) <br>

My code is [here](ll_merge/ll_merge.py)

## Solution
![ll_merge whiteboard image 1](assets/ll_merge_WB-1.png)
![ll_merge whiteboard image 2](assets/ll_merge_WB-2.png)


## ATTRIBUTIONS:
Many thanks to Skyler Burger and James Salamonsen for helping me dig out of the 'import' maze!

Submission PR:  https://github.com/vorSherer/Py-DSnA/pull/27

Checklist:

 - [X] Top-level README “Table of Contents” is updated
 - [X] Feature tasks for this challenge are completed
 - [ ] Unit tests written and passing
     - [ ] “Happy Path” - Expected outcome
     - [ ] Expected failure
     - [ ] Edge Case (if applicable/obvious)
 - [X] README for this challenge is complete
     - [X] Summary, Description, Approach & Efficiency, Solution
     - [X] Link to code
     - [X] Picture of whiteboard
