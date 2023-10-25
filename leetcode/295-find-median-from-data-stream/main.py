# Let n be the length of int_list


class MedianFinder:
    def __init__(self):
        self.int_list = []

    def addNum(self, num: int) -> None:
        # Time: O(n)
        # Space: O(1)
        for index, list_num in enumerate(self.int_list):
            if num < list_num:
                self.int_list.insert(index, num)
                return
        self.int_list.append(num)

    def findMedian(self) -> float:
        # Time: O(1)
        # Space: O(1)
        list_len = len(self.int_list)
        if list_len % 2 == 0:
            return (self.int_list[list_len // 2] + self.int_list[list_len // 2 - 1]) / 2
        return self.int_list[list_len // 2]
