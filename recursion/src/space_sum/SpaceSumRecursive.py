from src.space_sum.SpaceSum import SpaceSum


class SpaceSumRecursive(SpaceSum):
    """
    Object SpaceSum that using the recursive
    """
    def count(self, line: str):
        if " " not in line:
            return 0
        return self.__count_recursive(line, 0)

    def __count_recursive(self, line, i):
        if i >= len(line):
            return 0

        # previous
        # current
        # next

        a = 1 if line[i] == " " else 0
        return a + self.__count_recursive(line, i + 1)