# Time: O(n)
# Space: O(n)


class Solution:
    def __init__(self) -> None:
        self.uglies = [1]
        self.pointers = [0, 0, 0]  # 2, 3, 5

    def nthUglyNumber(self, n: int) -> int:
        length = len(self.uglies)
        while length < n:
            candidates = [
                self.uglies[self.pointers[0]] * 2,
                self.uglies[self.pointers[1]] * 3,
                self.uglies[self.pointers[2]] * 5,
            ]
            ugly = min(candidates)
            self.uglies.append(ugly)
            for i, c in enumerate(candidates):
                if ugly == c:
                    self.pointers[i] += 1
            length += 1

        return self.uglies[-1]
