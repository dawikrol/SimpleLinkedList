import time
from typing import List, MutableSequence

from linked_list import SimpleLinkedList


def measure_execution_time(func):
    """
    A decorator to measure the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


def compare_simple_linked_list_with_python_list(n: int = 1000) -> None:
    print("\nTest for Simple Linked List")
    linked_list = create_linked_list(n)
    iterate_list(linked_list)

    print("\nTest for Python List")
    python_list = create_python_list(n)
    iterate_list(python_list)


@measure_execution_time
def create_linked_list(num_elements) -> SimpleLinkedList:
    linked_list = SimpleLinkedList()
    for i in range(num_elements):
        linked_list.push(i)
    return linked_list


@measure_execution_time
def create_python_list(num_elements) -> List:
    python_list = list()
    for i in range(num_elements):
        python_list.append(i)
    return python_list


@measure_execution_time
def iterate_list(_list: MutableSequence) -> None:
    for i in range(len(_list)):
        _list.pop()


if __name__ == "__main__":
    compare_simple_linked_list_with_python_list()
