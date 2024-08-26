from abc import ABC, abstractmethod


class Sum(ABC):
    """
    Abstract object Sum that counts the Fibonacci number
    """
    @abstractmethod
    def fib(self, n: int) -> int:
        raise NotImplementedError
