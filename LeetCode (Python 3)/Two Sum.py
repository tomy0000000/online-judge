def binary_search_recursive(a_list, item):
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return -1
    else:
        i = (first + last) // 2
        if item == a_list[i][1]:
            return i
        else:
            if a_list[i][1] < item:
                tmp = binary_search_recursive(a_list[i+1:], item)
                return (i + 1 + tmp) if tmp != -1 else -1
            else:
                return binary_search_recursive(a_list[:i], item)

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_list = []
        for ind, val in enumerate(nums):
            new_list.append((ind, val))
        new_list.sort(key=lambda x: x[1])
        # print(new_list)
        for i, each in enumerate(new_list):
        #     print(each[1], target-each[1])
            ind = binary_search_recursive(new_list[i+1:], target-each[1])
        #     print("Theind: ",ind)
            if ind != -1:
                # print([each[0], new_list[i + 1 + ind][0]])
                return [each[0], new_list[i + 1 + ind][0]]
