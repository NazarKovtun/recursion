from src.factorial.Factorial import Factorial


class FactorialRecursive(Factorial):
    """
    Object Factorial that using the recursive
    """
    def f(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return n * self.f(n - 1)