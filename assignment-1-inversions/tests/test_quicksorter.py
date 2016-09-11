import unittest
from solution.quicksorter import QuickSorter


class QuicksorterTestCase(unittest.TestCase):
    unsorted = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    sorted = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]

    def test_sort(self):
        self.assertEqual(QuickSorter.sort(self.unsorted), self.sorted)

    def test_sort_empty(self):
        self.assertEqual(QuickSorter.sort([]), [])

    def test_sort_one_element(self):
        self.assertEqual(QuickSorter.sort([1]), [1])


if __name__ == '__main__':
    unittest.main()
