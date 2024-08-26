from src.factorial.Factorial import Factorial


class FactorialFor(Factorial):
    """
    Object Factorial that using the for loop
    """
    def f(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        acc = 1
        for num in range(2, n + 1):
            acc *= num
        return acc