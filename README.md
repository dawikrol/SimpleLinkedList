# Recruitment Task: Custom Singly Linked List Implementation

This repository contains a Python implementation of a custom singly linked list structure, created as part of a recruitment task. The task involves defining a data structure based on object-oriented programming principles with additional implementation details. The goal is to create a singly linked list that meets specific requirements and includes various methods for manipulation and traversal.

## Task Description

The task involves creating a custom singly linked list structure with the following features and methods:

1. The structure can only store values of the same data type.
2. The following methods should be implemented:

   - **push**: This method allows adding elements to the list. It should include the option to set a maximum length for the list. Once this maximum length is reached, new elements should not be added, and a `FullListError` should be raised.
   - **pop**: This method allows removing an element from the list based on the provided index, value, or all occurrences of a specific value. If no matching element or index is found, appropriate exceptions (`NoSuchElementError` or `NoSuchIndexError`) should be raised.
   - **print**: This method should print the entire list in a user-friendly manner on the console.

3. Implement tests to verify the correctness of the solution.
4. Implement the ability to iterate through the structure using a `for` loop by implementing generators/iterators.
5. Write a decorator to measure the execution time of a method and apply it to the traversal of the entire structure. Compare the execution time with that of a Python built-in list.
6. Create an instance of the custom linked list with 1000 elements and compare the traversal time with a Python built-in list.

## Usage

To use the custom singly linked list implementation and test its features, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Open the Python script containing the custom linked list implementation.
4. Use the provided methods to create, manipulate, and traverse the custom linked list.
5. Run the tests to ensure the correctness of the implementation.

## Credits

This project was created as a response to a recruitment task. Feel free to use, modify, and distribute this code according to the terms of the license provided.
If you discover any bugs or have suggestions for refactoring, improvements, or other ideas, please don't hesitate to get in touch with me. Your feedback is greatly appreciated!

---

*Note: This README provides a brief overview of the recruitment task and its requirements. For detailed implementation and code examples, please refer to the source code files in the repository.*