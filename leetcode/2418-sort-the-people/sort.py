# Let n be the length of names
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        index_names = [f"{i}-{n}" for i, n in enumerate(names)]
        height_dict = {n: h for n, h in zip(index_names, heights)}
        index_names.sort(key=lambda x: height_dict[x], reverse=True)
        return [n.split("-")[1] for n in index_names]
