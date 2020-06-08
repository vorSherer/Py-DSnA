# Shift Contents of an Array
Given a list and a value to be added to the middle of said list, write code to do so, shifting the remainder of the list up one index from where the value was added.

## Challenge Description
Write a function called insert_shift_array which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
I coded a floor division of the list length (+1 to account for odd index counts) and used a simple concatination to append the new value into the middle of the list. This approach works for integer and string content. <br>

Big O space for this approach is O(n) <br>
Big O time for this approach is O(n) <br>

## Solution
![array_shift Whiteboard part 1](/assets/array_shift_WB-1.png)
![array_shift Whiteboard part 2](/assets/array_shift_WB-2.png)

[My Code is here.](array_shift.py)


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


Pull Request submitted:  https://github.com/vorSherer/Py-DSnA/pull/10


## Collaboration and Attribution
Thanks to __*James Salamonsen*__ for help in resolving import issues! <br>
[Big O Cheatsheet](https://www.bigocheatsheet.com/) helped in determining *Big O* for this assignment. <br>
