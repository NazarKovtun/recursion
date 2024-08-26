from src.factorial.Factorial import Factorial


class FactorialWhileTail(Factorial):
    """
    Object Factorial that using the while tail loop
    """
    def f(self, n: int) -> int:
        if n == 0:
            return 0

        acc = 1
        while True:
            if n == 0:
                return acc
            (n, acc) = (n - 1, n * acc)