# Let n be the length of nums
#
# Time: O(n)
# Space: O(n)


class Sequence:
    def __init__(self, value: int):
        self.begin = value
        self.end = value

    def __len__(self) -> int:
        return self.end - self.begin + 1

    def __str__(self) -> str:
        return f"Sequence from {self.begin} to {self.end}"

    def __repr__(self) -> str:
        return f"<Sequence from {self.begin} to {self.end}>"

    def fit(self, value: int) -> bool:
        if value == self.begin - 1:
            self.begin -= 1
            return True
        if value == self.end + 1:
            self.end += 1
            return False
        raise ValueError(f"{value} does not fit in {self}")

    def concat(self, seq: "Sequence") -> bool:
        if self.end == seq.begin:
            self.end = seq.end
            return True
        if seq.end == self.begin:
            self.begin = seq.begin
            return False
        raise ValueError(f"{seq} can not concat with {self}")


class SequenceManager:
    def __init__(self):
        self.seqs: list[Sequence] = []

        # This is a dirty table
        # should only expect edge to points to the right sequences
        self.table: dict[int, list[Sequence]] = {}

        # True for edge, False for inner
        self.types: dict[int, bool] = {}

    def index_table(self, value: int, new_seq: Sequence):
        if value in self.table:
            self.table[value].append(new_seq)
        else:
            self.table[value] = [new_seq]

    def fit(self, value: int):
        if value in self.types:
            if self.types[value]:
                if len(self.table[value]) == 1:
                    # Extending sequence by one
                    target_seq = self.table[value][0]
                    extend_at_begin = target_seq.fit(value)

                    if extend_at_begin:
                        self.types[value - 1] = True
                        self.index_table(value - 1, target_seq)
                    else:
                        self.types[value + 1] = True
                        self.index_table(value + 1, target_seq)
                elif len(self.table[value]) == 2:
                    # Filling the remaining gap to concat two sequence
                    seq_one = self.table[value][0]
                    seq_two = self.table[value][1]

                    seq_one.fit(value)
                    seq_two.fit(value)

                    self.seqs.remove(seq_two)

                    if seq_one.concat(seq_two):
                        self.table[seq_two.end + 1].remove(seq_two)
                        self.table[seq_two.end + 1].append(seq_one)
                    else:
                        self.table[seq_two.begin - 1].remove(seq_two)
                        self.table[seq_two.begin - 1].append(seq_one)
        else:
            new_seq = Sequence(value)
            self.seqs.append(new_seq)
            for i in range(value - 1, value + 2):  # value - 1 to value + 1
                self.index_table(i, new_seq)
            self.types[value - 1] = True
            self.types[value + 1] = True

        self.types[value] = False


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        pool = SequenceManager()
        for n in nums:
            pool.fit(n)

        return len(max(pool.seqs, key=len))
