from unittest import TestCase

from src.factorial.FactorialRecursiveTail import FactorialRecursiveTail


class TestFactorialRecursiveTail(TestCase):
    """
    Test for the object Factorial that using the recursive tail
    """
    def setUp(self):
        self.sut = FactorialRecursiveTail()

    def test_f_0_result_0(self):
        self.assertEqual(0, self.sut.f(0))

    def test_f_1_result_1(self):
        self.assertEqual(1, self.sut.f(1))

    def test_f_2_result_2(self):
        self.assertEqual(2, self.sut.f(2))

    def test_f_3_result_6(self):
        self.assertEqual(6, self.sut.f(3))

    def test_f_4_result_24(self):
        self.assertEqual(24, self.sut.f(4))

    def test_f_5_result_120(self):
        self.assertEqual(120, self.sut.f(5))