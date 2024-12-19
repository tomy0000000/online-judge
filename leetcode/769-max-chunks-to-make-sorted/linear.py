# Let n be the length of arr
#
# Time: O(n)
# Space: O(n)


class Solution:
    def valid_chunk(self, chunk, start):
        for i in range(start, start + len(chunk)):
            if i not in chunk:
                return False
        return True

    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        chunk = set()
        chunk_count = 0
        for i in range(n - 1, -1, -1):
            chunk.add(arr[i])
            if self.valid_chunk(chunk, i):
                chunk.clear()
                chunk_count += 1
        return chunk_count
