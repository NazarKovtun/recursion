from abc import ABC, abstractmethod


class Factorial(ABC):
    """
    Abstract object Factorial
    """
    @abstractmethod
    def find_fac(self, n: int) -> int:
        raise NotImplementedError
