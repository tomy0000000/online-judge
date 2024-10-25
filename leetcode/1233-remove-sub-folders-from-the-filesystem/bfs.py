# Let n be the length of folder
#
# Time: O(n)
# Space: O(n)

from collections import deque


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        system = {}
        for f in folder:
            path = f[1:].split("/")
            here = system
            for p in path:
                if "exist" in here:
                    break
                if p not in here:
                    here[p] = {}
                here = here[p]
            here["exist"] = True

        queue = deque([(system, "")])
        ans = []
        while queue:
            here, path = queue.popleft()
            for name, dirs in here.items():
                new_path = f"{path}/{name}"
                if "exist" in dirs:
                    ans.append(new_path)
                else:
                    queue.append((dirs, new_path))

        return ans
