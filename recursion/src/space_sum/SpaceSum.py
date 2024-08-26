from abc import ABC, abstractmethod


class SpaceSum(ABC):
    """
    Abstract object SpaceSum that counts the number of space in a string
    """
    @abstractmethod
    def count(self, line: str) -> int:
        raise NotImplementedError