from typing import List


class Solution:

  def shiftAll(self, matrix: List[List[int]], x0: int, y0: int, x1: int,
               y1: int, x2: int, y2: int, x3: int, y3: int):
    temp = matrix[x0][y0]
    matrix[x0][y0] = matrix[x1][y1]
    matrix[x1][y1] = matrix[x2][y2]
    matrix[x2][y2] = matrix[x3][y3]
    matrix[x3][y3] = temp

  def rotate(self, matrix: List[List[int]]) -> None:
    size = len(matrix) - 1
    middle = (size) / 2

    shift = 1 if len(matrix) % 2 == 0 else 0

    for x in range(int(middle) + shift):
      for y in range(int(middle) + 1):
        # print('%d %d (x,y)' % (x, y))

        x1 = size - y
        y1 = x
        # print('%d %d (x1,y1) %.04f %.04f' % (round(x1, 0), round(y1, 0), x1, y1))

        x2 = size - x
        y2 = size - y
        # print('%d %d (x2,y2) %.04f %.04f' % (round(x2, 0), round(y2, 0), x2, y2))

        x3 = y
        y3 = size - x
        # print('%d %d (x3,y3) %.04f %.04f' % (round(x3, 0), round(y3, 0), x3, y3))
        # print('')

        self.shiftAll(matrix, x, y, x1, y1, x2, y2, x3, y3)


my = Solution()
# n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print("n before", n)
my.rotate(n)
print("n after", n)

# Runtime: 32 ms, faster than 78.58% of Python3 online submissions for Rotate Image.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Rotate Image.

#     0 1 2 3
# 0 | 1 2 3 4
# 1 | 4 5 6 7
# 2 | 7 8 9 9
# 3 | 9 9 8 2

# 0 1 => 2 0 => 3 2 => 1 3
# 1 0 => 3 1 => 2 3 => 0 2

#     0 1 2
# 0 | 1 2 3
# 1 | 4 5 6
# 2 | 7 8 9

# 0 1
# 3/2 = 1/1

# First
# 1,1 - 0,1 = 1,0
# width = 1
# 0,1 + 1,-1 = 1,0
# down => left

# 0,0 1,1
# x,y xC,yC

# xD,xY = xC - x, yC - y
# 1,1

# x1 = xC - xD
# y1 = yC + yD

# x2 = xC + xD
# y2 = yC + yD
# 2,2

# x3 = xC - xD
# y3 = yC + yD
# 0,2

# 0 0 -> 2 0 -> 2 2 -> 0 2
# point -  0 0
# center - 1 1
# diff vector - ((0 - 1)^2 - (0 - 1)^2) =

# 0 1 -> 1 0 -> 2 1 -> 1 2