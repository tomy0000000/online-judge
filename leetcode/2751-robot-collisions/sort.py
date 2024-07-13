# Let n be the length of positions, healths, and directions.
#
# Time: O(n log n)
# Space: O(n)


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        robots = [
            {"ind": i, "pos": pos, "health": health, "dir": face}
            for i, pos, health, face in zip(
                range(len(positions)), positions, healths, directions
            )
        ]
        robots.sort(key=lambda x: x["pos"])
        dirs = "".join(r["dir"] for r in robots)
        while True:
            r1 = dirs.find("RL")
            if r1 == -1:
                break
            r2 = r1 + 1
            r1h, r2h = robots[r1]["health"], robots[r2]["health"]
            if r1h == r2h:
                robots.pop(r2)
                robots.pop(r1)
                dirs = dirs[:r1] + dirs[r2 + 1 :]
            elif r1h < r2h:
                robots[r2]["health"] -= 1
                robots.pop(r1)
                dirs = dirs[:r1] + dirs[r1 + 1 :]
            elif r1h > r2h:
                robots[r1]["health"] -= 1
                robots.pop(r2)
                dirs = dirs[:r2] + dirs[r2 + 1 :]
        robots.sort(key=lambda x: x["ind"])
        return [r["health"] for r in robots]
