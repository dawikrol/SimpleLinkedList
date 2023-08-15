import unittest

from excepctions import FullListError, NoSuchIndexError, NoSuchElementError
from linked_list import SimpleLinkedList


class TestSimpleLinkedList(unittest.TestCase):

    def test_empty_list(self):
        simple_linked_list = SimpleLinkedList()

        self.assertEqual(simple_linked_list.length, 0)
        self.assertEqual(str(simple_linked_list), "")

    def test_push_single_type(self):
        simple_linked_list = SimpleLinkedList()

        simple_linked_list.push(5)
        simple_linked_list.push(10)
        simple_linked_list.push(15)

        self.assertEqual(simple_linked_list.length, 3)
        self.assertEqual(simple_linked_list.data_type, int)
        self.assertEqual(str(simple_linked_list), "5 -> 10 -> 15")

    def test_push_different_types(self):
        simple_linked_list = SimpleLinkedList()

        simple_linked_list.push("apple")
        simple_linked_list.push("banana")
        simple_linked_list.push("cherry")

        self.assertEqual(simple_linked_list.length, 3)
        self.assertEqual(simple_linked_list.data_type, str)
        self.assertEqual(str(simple_linked_list), "apple -> banana -> cherry")

        with self.assertRaises(ValueError):
            simple_linked_list.push(5)

    def test_max_length(self):
        simple_linked_list = SimpleLinkedList(max_length=2)

        simple_linked_list.push(5)
        simple_linked_list.push(10)

        with self.assertRaises(FullListError):
            simple_linked_list.push(15)

        self.assertEqual(simple_linked_list.length, 2)

    def test_pop_by_index(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.push(5)
        simple_linked_list.push(10)
        simple_linked_list.push(15)

        self.assertEqual(simple_linked_list.pop(index=1), 10)
        self.assertEqual(simple_linked_list.length, 2)
        self.assertEqual(str(simple_linked_list), "5 -> 15")

    def test_pop_by_value_single_occurrence(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.push("apple")
        simple_linked_list.push("banana")
        simple_linked_list.push("cherry")
        simple_linked_list.push("banana")

        self.assertEqual(simple_linked_list.pop(value="banana"), "banana")
        self.assertEqual(simple_linked_list.length, 3)
        self.assertEqual(str(simple_linked_list), "apple -> cherry -> banana")

    def test_pop_by_value_all_occurrences(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.push("apple")
        simple_linked_list.push("banana")
        simple_linked_list.push("banana")
        simple_linked_list.push("cherry")

        self.assertEqual(simple_linked_list.pop(value="banana", all_occurrences=True), ["banana", "banana"])
        self.assertEqual(simple_linked_list.length, 2)
        self.assertEqual(str(simple_linked_list), "apple -> cherry")

    def test_pop_empty_list(self):
        simple_linked_list = SimpleLinkedList()

        with self.assertRaises(NoSuchIndexError):
            simple_linked_list.pop(index=0)

    def test_pop_not_existed_value(self):
        simple_linked_list = SimpleLinkedList()

        with self.assertRaises(NoSuchElementError):
            simple_linked_list.pop(value="apple")

    def test_pop_invalid_index(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.push(5)

        with self.assertRaises(NoSuchIndexError):
            simple_linked_list.pop(index=1)

    def test_iteration(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.push(10)
        simple_linked_list.push(20)
        simple_linked_list.push(30)

        expected_values = [10, 20, 30]
        for idx, item in enumerate(simple_linked_list):
            self.assertEqual(item, expected_values[idx])
