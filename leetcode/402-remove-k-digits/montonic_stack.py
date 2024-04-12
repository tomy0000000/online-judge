# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while stack and k and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        stack = stack[:-k] if k > 0 else stack

        return "".join(stack).lstrip("0") or "0"
