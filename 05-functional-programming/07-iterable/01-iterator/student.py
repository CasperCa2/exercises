

class InclusiveRange():

    def __init__(self, start, end):
        self.__start_index = start
        self.__end_index = end

    def __iter__(self):
        return InclusiveRangeIterator(self.__start_index, self.__end_index)


class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.__current = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current <= self.__end:
            result = self.__current
            self.__current += 1
            return result
        else:
            raise StopIteration()
