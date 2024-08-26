from src.space_sum.SpaceSum import SpaceSum


class SpaceSumFor(SpaceSum):
    """
    Object SpaceSum that using the for loop
    """
    def count(self, line: str) -> int:
        acc = 0
        for i in line:
            if i == " ":
                acc += 1
        return acc