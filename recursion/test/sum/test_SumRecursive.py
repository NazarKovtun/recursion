from unittest import TestCase

from src.sum.SumRecursive import SumRecursive


class TestSumRecursive(TestCase):
    """
    Test for the object Sum that using the recursive
    """
    def setUp(self):
        self.sut = SumRecursive()

    def test_f_n1_result_0(self):
        self.assertEqual(0, self.sut.fib(-1))

    def test_f_0_result_0(self):
        self.assertEqual(0, self.sut.fib(0))

    def test_f_1_result_1(self):
        self.assertEqual(1, self.sut.fib(1))

    def test_f_2_result_3(self):
        self.assertEqual(3, self.sut.fib(2))
