# Let n be the length of s
#
# Time: O(n)
# Space: O(1)


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stacks = [0]
        for c, l in zip(s, locked):
            if l == "0":
                new_stacks = set()
                for stack in stacks[:10]:
                    new_stacks.add(stack - 1)
                    new_stacks.add(stack + 1)
                stacks = [stack for stack in new_stacks if 0 <= stack]
            if l == "1":
                if c == "(":
                    stacks = [stack + 1 for stack in stacks]
                if c == ")":
                    stacks = [stack - 1 for stack in stacks if stack != 0]
        return 0 in stacks
