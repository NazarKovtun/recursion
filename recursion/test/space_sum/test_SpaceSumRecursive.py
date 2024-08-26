from unittest import TestCase

from src.space_sum.SpaceSumRecursive import SpaceSumRecursive


class TestSpaceSumRecursive(TestCase):
    """
    Test for the object SpaceSum that using the recursive
    """
    def setUp(self):
        self.sut = SpaceSumRecursive()

    def test_f_1_result_1(self):
        self.assertEqual(1, self.sut.count("1 "))

    def test_f_2_result_2(self):
        self.assertEqual(2, self.sut.count("1 2 "))
