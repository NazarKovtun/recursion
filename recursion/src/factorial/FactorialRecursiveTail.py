from src.factorial.Factorial import Factorial


class FactorialRecursiveTail(Factorial):
    """
    Object Factorial that using the recursive tail
    """
    def f(self, n: int) -> int:
        if n == 0:
            return 0
        return self.__f_recursive(n, 1)

    def __f_recursive(self, n: int, acc: int) -> int:
        if n == 0:
            return acc
        return self.__f_recursive(n - 1, n * acc)