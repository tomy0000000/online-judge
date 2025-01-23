# Let n be the number of cells in the grid
#
# Time: O(n)
# Space: O(n)


class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        connected = 0
        conn_cols = set()
        not_connected = set()
        for row in grid:
            summ = sum(row)
            if summ == 0:
                continue

            if summ == 1:
                index = row.index(1)
                if index in conn_cols:
                    connected += 1
                elif index in not_connected:
                    connected += 2
                    not_connected.remove(index)
                    conn_cols.add(index)
                else:
                    not_connected.add(index)
                continue

            for index in range(len(row)):
                if row[index] == 0:
                    continue

                conn_cols.add(index)
                connected += 1
                if index in not_connected:
                    connected += 1
                    not_connected.remove(index)

        return connected
