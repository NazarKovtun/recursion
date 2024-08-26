from src.sum.Sum import Sum


class SumFor(Sum):
    """
    Object Sum that using the for loop
    """
    def fib(self, n: int) -> int:
        acc = 0
        for i in range(n + 1):
            acc += i
        return acc