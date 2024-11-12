# Let n be the length of firstList and m be the length of secondList
#
# Time: O(n + m)
# Space: O(n + m))


class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        l1, l2 = len(firstList), len(secondList)
        ptr_1, ptr_2 = 0, 0
        merged = []
        while ptr_1 < l1 and ptr_2 < l2:
            if firstList[ptr_1][1] < secondList[ptr_2][0]:
                ptr_1 += 1
                continue
            if secondList[ptr_2][1] < firstList[ptr_1][0]:
                ptr_2 += 1
                continue

            interval = [0, 0]

            if firstList[ptr_1][0] < secondList[ptr_2][0]:
                interval[0] = secondList[ptr_2][0]
            else:
                interval[0] = firstList[ptr_1][0]

            if firstList[ptr_1][1] < secondList[ptr_2][1]:
                interval[1] = firstList[ptr_1][1]
                ptr_1 += 1
            else:
                interval[1] = secondList[ptr_2][1]
                ptr_2 += 1

            merged.append(interval)

        return merged
