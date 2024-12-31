# README: Python List Operations

## Overview
This project demonstrates basic list operations in Python, including appending, inserting, extending, removing, sorting, and finding the index of an element. The code is beginner-friendly and serves as an introduction to manipulating Python lists.

## Steps

1. **Create an empty list**:
   An empty list called `my_list` is created to store elements.

2. **Append elements**:
   Elements `10`, `20`, `30`, and `40` are added to the list using the `append` method.

3. **Insert an element**:
   The value `15` is inserted at the second position (index 1) using the `insert` method.

4. **Extend the list**:
   The list is extended by adding elements from another list `[50, 60, 70]` using the `extend` method.

5. **Remove the last element**:
   The last element is removed using the `pop` method.

6. **Sort the list**:
   The list is sorted in ascending order using the `sort` method.

7. **Find and print the index of a value**:
   The index of the value `30` is found using the `index` method and printed to the console.

8. **Print the final list**:
   The final state of the list is printed.

## How to Run
1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Copy the code below into a Python file (e.g., `list_operations.py`):

   ```python
   # Step 1: Create an empty list
   my_list = []

   # Step 2: Append elements 10, 20, 30, 40 to the list
   my_list.append(10)
   my_list.append(20)
   my_list.append(30)
   my_list.append(40)

   # Step 3: Insert the value 15 at the second position (index 1)
   my_list.insert(1, 15)

   # Step 4: Extend the list with another list [50, 60, 70]
   my_list.extend([50, 60, 70])

   # Step 5: Remove the last element from the list
   my_list.pop()

   # Step 6: Sort the list in ascending order
   my_list.sort()

   # Step 7: Find and print the index of the value 30 in the list
   index_of_30 = my_list.index(30)
   print(f"The index of 30 in the list is: {index_of_30}")

   # Print the final list
   print("Final list:", my_list)
   ```

3. Open a terminal or command prompt, navigate to the directory containing the file, and run the script:

   ```bash
   python list_operations.py
   ```

4. View the output in the terminal.

## Expected Output
```
The index of 30 in the list is: 3
Final list: [10, 15, 20, 30, 40, 50, 60]
```

## Learnings
- **Creating a list**: Understand how to initialize an empty list.
- **Modifying lists**: Use methods like `append`, `insert`, and `extend` to add elements.
- **Removing elements**: Use the `pop` method to remove elements.
- **Sorting a list**: Use the `sort` method to arrange elements in ascending order.
- **Accessing elements**: Use the `index` method to find the position of an element in the list.

## Conclusion
This project is a simple introduction to Python list operations, helping beginners learn the basics of list manipulation in Python.

