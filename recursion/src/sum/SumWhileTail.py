from src.sum.Sum import Sum


class SumWhileTail(Sum):
    """
    Object Sum that using the while tail
    """
    def fib(self, n: int) -> int:
        if n < 1:
            return 0

        acc = 0
        while True:
            if n < 1:
                return acc
            (n, acc) = (n - 1, n + acc)