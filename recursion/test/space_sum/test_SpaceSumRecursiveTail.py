from unittest import TestCase

from src.space_sum.SpaceSumRecursiveTail import SpaceSumRecursiveTail


class TestSpaceSumRecursiveTail(TestCase):
    """
    Test for the object SpaceSum that using the recursive tail
    """
    def setUp(self):
        self.sut = SpaceSumRecursiveTail()

    def test_f_0_result_0(self):
        self.assertEqual(0, self.sut.count("0"))

    def test_f_1_result_1(self):
        self.assertEqual(1, self.sut.count("1 "))

    def test_f_2_result_2(self):
        self.assertEqual(2, self.sut.count("1 2 "))

    def test_f_5_result_5(self):
        self.assertEqual(5, self.sut.count("1 2 3 4 5 "))

