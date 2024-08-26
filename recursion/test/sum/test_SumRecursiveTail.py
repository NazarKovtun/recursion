from unittest import TestCase

from src.sum.SumRecursiveTail import SumRecursiveTail


class TestSumRecursiveTail(TestCase):
    """
    Test for the object Sum that using the recursive tail
    """
    def setUp(self):
        self.sut = SumRecursiveTail()

    def test_f_n1_result_0(self):
        self.assertEqual(0, self.sut.fib(-1))

    def test_f_0_result_0(self):
        self.assertEqual(0, self.sut.fib(0))

    def test_f_1_result_1(self):
        self.assertEqual(1, self.sut.fib(1))

    def test_f_2_result_3(self):
        self.assertEqual(3, self.sut.fib(2))

    def test_f_3_result_6(self):
        self.assertEqual(6, self.sut.fib(3))