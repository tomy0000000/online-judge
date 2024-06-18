# Let n be the max number of jobs and workers.
#
# Time: O(n log n)
# Space: O(1)

from collections import Counter


class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        jobs = sorted((d, p) for d, p in zip(difficulty, profit))
        c = Counter(worker)
        abilities = sorted(c)

        job_count = len(jobs)
        index = 0
        maxi = 0
        profit = 0
        for ability in abilities:
            while index < job_count and jobs[index][0] <= ability:
                maxi = max(maxi, jobs[index][1])
                index += 1
            profit += maxi * c[ability]

        return profit
