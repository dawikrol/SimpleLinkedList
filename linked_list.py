from typing import Any, Optional

from excepctions import FullListError, NoSuchElementError, NoSuchIndexError


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class SimpleLinkedList:
    """
    A Simple Linked List implementation for storing objects of the same type.

    Properties
    ----------
    max_length : int or None, optional
        The maximum capacity of the linked list. If specified, the linked list will not
        allow more than `max_length` elements. If not specified, the linked list can grow
        without bound.

    data_type : type
        The data type of the linked list's elements. It's automatically determined when
        the first element is pushed into the list. All subsequent elements must match
        this data type.

    length : int
        The number of elements in the linked list.

    Methods
    -------
    push(self, data)
        Push a new element with the given data to the end of the linked list.

    pop(self, index: int = 0, value=None, all_occurrences=False)
        Remove an element from the linked list based on the provided criteria.
    """

    def __init__(self, max_length: Optional[int] = None):
        self.__max_length = max_length
        self.__data_type = None
        self.__head = None
        self.__length = 0

    def __str__(self):
        elements = []
        current = self.__head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)

    def __iter__(self):
        current = self.__head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self.length

    @property
    def max_length(self) -> Optional[int]:
        return self.__max_length

    @property
    def data_type(self) -> Optional[type]:
        return self.__data_type

    @property
    def length(self) -> int:
        return self.__length

    def push(self, data):
        """
        Push a new element to the end of the linked list.

        Args:
            data: The data to be added to the linked list.

        Raises:
            FullListError: If the linked list has reached its maximum capacity.
            ValueError: If the data type of the input does not match the expected data type.
        """

        if self.max_length is not None and self.length >= self.max_length:
            raise FullListError(f"The linked list has reached its maximum capacity. Max size {self.__max_length}")

        if self.data_type is None:
            self.__data_type = type(data)

        if not isinstance(data, self.data_type):
            raise ValueError(f"Data type mismatch. Required data type: {self.data_type}")

        new_node = Node(data)
        if not self.__head:
            self.__head = new_node
        else:
            current_node = self.__head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.__length += 1

    def pop(self, index: Optional[int] = None, value: Any = None, all_occurrences: bool = False) -> Any:
        """
          Pop an item from the list based on the provided index or value.

          Args:
              index (int, optional): Index of the item to be popped. Defaults to None.
              value (Any, optional): Value of the item to be popped. Defaults to None.
              all_occurrences (bool, optional): Flag to indicate if all occurrences should be considered.
                  Defaults to False.

          Returns:
              Any: The result of popping the item.
          """

        if index is not None and (index < 0 or index >= self.length):
            raise NoSuchIndexError("Index out of range")

        if not index and not value and not all_occurrences:
            return self._default_handler()

        if index is not None:
            return self._index_handler(index)

        if value is not None:
            return self._value_handler(value, all_occurrences)

    def _default_handler(self) -> Any:
        data = self.__head.value
        self.__head = self.__head.next
        self.__length -= 1
        return data

    def _index_handler(self, index: int) -> Any:
        if index == 0:
            data = self.__head.value
            self.__head = self.__head.next
        else:
            previous_node = self._get_node_at_index(index - 1)
            popped_element = previous_node.next
            data = popped_element.value
            previous_node.next = popped_element.next

        self.__length -= 1
        return data

    def _get_node_at_index(self, index: int) -> Node:
        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def _value_handler(self, value: Any, all_occurrences: bool) -> Any:
        popped_values = []

        previous_node = None
        current_node = self.__head

        while current_node:
            if current_node.value == value:
                if previous_node is None:
                    self.__head = current_node.next
                else:
                    previous_node.next = current_node.next

                popped_values.append(current_node.value)

                if not all_occurrences:
                    break  # Exit loop after removing the first occurrence
            else:
                previous_node = current_node

            current_node = current_node.next

        if popped_values:
            self.__length -= len(popped_values)  # Correctly update the length
            return popped_values if all_occurrences else popped_values[0]
        else:
            raise NoSuchElementError("Element not found")
