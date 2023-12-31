from typing import List


class Solution:
    def isWinner(player1: List[int], player2: List[int]) -> int:
        def f(arr: List[int]) -> int:
            s = 0
            for i, x in enumerate(arr):
                k = 2 if (i and arr[i - 1] == 10) or (i > 1 and arr[i - 2] == 10) else 1
                s += k * x
            return s

        a, b = f(player1), f(player2)
        return 1 if a > b else (2 if b > a else 0)


if __name__ == "__main__":
    p1 = [5,6,1,10]
    p2 = [5,1,10,5]
    print(Solution.isWinner(p1, p2))