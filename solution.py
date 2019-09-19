from typing import List


class Solution(object):
    def solve(self, circuit: List[int]) -> int:
        if(len(circuit) == 0):
            return 0

        total = 0
        state = list(map(lambda x: False, circuit))
        i = 0

        for value in circuit:
            # If the switch index is longer than the circuit could possibly represent, ignore it
            if value >= len(state):
                continue

            state[value] = True

            while i < len(state) and state[i]:
                i += 1

            if i >= value:
                total += 1

        return total
