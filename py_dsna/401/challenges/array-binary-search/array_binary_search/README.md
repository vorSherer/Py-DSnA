# Binary Search of an Array
Given a list and a value to be used as a search key, use a binary search methodology to determine whether the search key value exists in the array.

## Challenge Description
Write a function called BinarySearch (changed to "binary_search" to be pythonic) which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
I decided upon an iterative approach to perform the binary search. <br>

Big O space for this approach is O(n) <br>
Big O time for this approach is O(log(n) <br>

## Solution
![array_binary_search Whiteboard part 1](./assets/array_binary_search_WB-1.png)
![array_binary_search Whiteboard part 2](./assets/array_binary_search_WB-2.png)

[My Code is here.](array_binary_search.py)


## Task Checklist: <br>
- [X] Top-level README “Table of Contents” is updated <br>
- [X] Feature tasks for this challenge are completed <br>
- [X] Unit tests written and passing <br>
    - [X] “Happy Path” - Expected outcome <br>
    - [X] Expected failure <br>
    - [X] Edge Case (if applicable/obvious) <br>
- [X] README for this challenge is complete <br>
    - [X] Summary, Description, Approach & Efficiency, Solution <br>
    - [X] Link to code <br>
    - [X] Pictures of whiteboard <br>


Pull Request submitted: https://github.com/vorSherer/Py-DSnA/pull/11


## Collaboration and Attribution
Thanks to __*Skyler Burger*__ for help with list comprehensions (*after* I brute-force created a list of 100000 elements!) <br>
[Big O Cheatsheet](https://www.bigocheatsheet.com/) helped in determining *Big O* for this assignment. <br>
