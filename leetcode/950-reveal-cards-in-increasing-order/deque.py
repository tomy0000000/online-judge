# Let n be the length of deck
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        new_deck = deque()
        while deck:
            new_deck.appendleft(deck.pop())
            new_deck.rotate()
        new_deck.rotate(-1)
        return new_deck
