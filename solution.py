from typing import List


class Solution(object):
    def solve(self, circuit: List[int]) -> int:
        if(len(circuit) == 0):
            return 0

        total = 0

        is_set = set()

        for value in circuit:
            is_set.add(value)

            success = True
            for i in range(0, value):
                if i not in is_set:
                    success = False

            if success:
                total += 1

        return total
