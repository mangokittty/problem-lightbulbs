import pytest
from solution import Solution


def test_solution():
    sol = Solution()

    assert sol.solve([]) == 0
    assert sol.solve([0]) == 1
    assert sol.solve([1]) == 0
    assert sol.solve([0, 1, 2]) == 3
    assert sol.solve([0, 2, 1]) == 2
    assert sol.solve([2, 1, 0]) == 1
    assert sol.solve([2, 0, 1]) == 2

    assert sol.solve(list(range(10, 20)) + list(range(0, 10))) == 10
