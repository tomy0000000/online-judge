# Let n be the length of bills
#
# Time: O(n)
# Space: O(1)


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        changes = {20: 0, 10: 0, 5: 0}
        for b in bills:
            changes[b] += 1
            to_change = b - 5
            while to_change:
                for c, num in changes.items():
                    if num == 0:
                        continue
                    if to_change < c:
                        continue
                    changes[c] -= 1
                    to_change -= c
                    break
                else:
                    return False
        return True
