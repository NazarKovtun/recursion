from src.space_sum.SpaceSum import SpaceSum


class SpaceSumWhileTail(SpaceSum):
    """
    Object SpaceSum that using the while tail loop
    """
    def count(self, line: str) -> int:
        if " " not in line:
            return 0

        i = 0
        acc = 0
        while True:
            if i >= len(line):
                return acc
            if line[i] == " ":
                acc += 1
            (i, acc) = (i + 1, acc)