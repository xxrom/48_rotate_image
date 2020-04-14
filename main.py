from typing import List


class Solution:

  def rotate(self, matrix: List[List[int]]) -> None:
    """
        Do not return anything, modify matrix in-place instead.
        """


my = Solution()
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("n before", n)
my.rotate(n)
print("n after", n)

    0 1 2
0 | 1 2 3
1 | 4 5 6
2 | 7 8 9

0 0 -> 2 0 -> 2 2 -> 0 2
point -  0 0
center - 1 1
diff vector - ((0 - 1)^2 - (0 - 1)^2) =

0 1 -> 1 0 -> 2 1 -> 1 2
