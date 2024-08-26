from src.space_sum.SpaceSum import SpaceSum


class SpaceSumRecursiveTail(SpaceSum):
    """
    Object SpaceSum that using the recursive tail
    """
    def count(self, line: str):
        if " " not in line:
            return 0
        return self.__count_recursive(line, 0, 0)

    def __count_recursive(self, line, i, acc):
        if i >= len(line):
            return acc
        if line[i] == " ":
            acc += 1
        return self.__count_recursive(line, i + 1, acc)