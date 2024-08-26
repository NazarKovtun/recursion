from src.sum.Sum import Sum


class SumRecursiveTail(Sum):
    """
    Object Sum that using the recursive tail
    """
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        return self.__f_recursive(n, 0)

    def __f_recursive(self, i: int, acc: int) -> int:
        if i < 1:
            return acc
        return self.__f_recursive(i - 1, i + acc)
