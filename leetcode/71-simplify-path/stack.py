# Let n be the length of path
#
# Time: O(n)
# Space: O(n)


class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified = []
        segments = path.split("/")
        for seg in segments:
            if not seg:
                continue
            if seg == ".":
                continue
            if seg == "..":
                if simplified:
                    simplified.pop()
                continue
            simplified.append(seg)

        return "/" + "/".join(simplified) if simplified else "/"
