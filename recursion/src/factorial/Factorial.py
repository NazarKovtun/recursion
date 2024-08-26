from abc import ABC, abstractmethod


class Factorial(ABC):
    """
    Abstract object Factorial
    """
    @abstractmethod
    def f(self, n: int) -> int:
        raise NotImplementedError
