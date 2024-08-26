from src.sum.Sum import Sum


class SumRecursive(Sum):
    """
    Object Sum that using the recursive
    """
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        return n + self.fib(n - 1)
