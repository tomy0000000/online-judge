# Let n be the length of stones
#
# Time: O(n)
# Space: O(n)


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        islands_row = {}
        islands_col = {}
        islands = {}
        n_island = 0
        island_counter = 0
        for i, j in stones:
            row, col = None, None
            if i in islands_row:
                row = islands_row[i]
            if j in islands_col:
                col = islands_col[j]

            island = None
            if row is not None and col is not None:
                while islands[row] is not None:
                    row = islands[row]
                while islands[col] is not None:
                    col = islands[col]

                if row == col:
                    continue

                islands[row] = col
                island = col
                n_island -= 1

            if row is not None:
                island = row
            elif col is not None:
                island = col
            else:
                island = island_counter
                islands[island_counter] = None
                island_counter += 1
                n_island += 1

            islands_row[i] = island
            islands_col[j] = island

        return len(stones) - n_island
