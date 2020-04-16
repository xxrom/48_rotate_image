from typing import List
import math


class Solution:

  def rotate(self, matrix: List[List[int]]) -> None:
    size = len(matrix)
    middle = int(size / 2)
    print('middle %d' % middle)

    def calcVectorSize(x0, y0, x1, y1):
      return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

    def getNextIndex(currentIndex: int, changeValue=0, size=0):
      if (size == 0):
        return currentIndex

      return (currentIndex + changeValue) % size

    print('sin %f' % math.sin(math.pi / 2))

    startPoint = [0, 0]

    xC = middle
    yC = middle
    '''
    1 2 3 4
    5 6 7 8
    9 9 9 9
    3 3 3 3

    [0,1] = from center [2,2]
    calc 'diff' and then
    find next 4 points
    by adding 'diff'
    plus adding shift individually
    by x and y lines
    '''

    for x in range(middle + 1):
      for y in range(middle):
        print('%d %d (x,y)' % (x, y))

        xD = xC - x
        yD = yC - y
        diff = math.sqrt(xD**2 + yD**2)
        print('diff', diff)

        x1 = xC + diff - abs(y)
        y1 = yC - diff - abs(x)
        print('%d %d (x1,y1)' % (x1, y1))

        x2 = xC + diff - abs(x)
        y2 = yC + diff - abs(y)
        print('%d %d (x2,y2)' % (x2, y2))

        x3 = xC - diff - abs(y)
        y3 = yC + diff - abs(x)
        print('%d %d (x3,y3)' % (x3, y3))

        print('')


my = Solution()
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("n before", n)
my.rotate(n)
print("n after", n)

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