# Let n be the length of hand
#
# Time: O(n ^ 2)
# Space: O(1)


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        hand.sort()
        while hand:
            base = hand[0]
            for i in range(groupSize):
                if base + i in hand:
                    hand.remove(base + i)
                else:
                    return False
        return True
