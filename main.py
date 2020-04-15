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
    middlePoint = [middle, middle]
    vectorSize = calcVectorSize(startPoint[0], startPoint[1], middlePoint[0],
                                middlePoint[1])
    print('vectSize %f' % vectorSize)
    # TODO: turn vector TO pi/2  =) that is all

    for i in range(middle + 1):
      for j in range(middle):
        print('%d %d (i,j)' % (i, j))

        i1 = getNextIndex(i, size - 1, size)
        j1 = getNextIndex(j, 0)
        print('%d %d (i1,j1)' % (i1, j1))

        i2 = getNextIndex(i1)
        j2 = getNextIndex(j1, size - 1, size)
        print('%d %d (i2,j2)' % (i2, j2))

        i3 = getNextIndex(i2, -(size - 1), size)
        j3 = getNextIndex(j2)
        print('%d %d (i3,j3)' % (i3, j3))

        i4 = getNextIndex(i3)
        j4 = getNextIndex(j3, -(size - 1), size)
        print('%d %d (i4,j4)' % (i4, j4))

        print('')


my = Solution()
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("n before", n)
my.rotate(n)
print("n after", n)
'''md
    0 1 2
0 | 1 2 3
1 | 4 5 6
2 | 7 8 9

0 0 -> 2 0 -> 2 2 -> 0 2
point -  0 0
center - 1 1
diff vector - ((0 - 1)^2 - (0 - 1)^2) =

0 1 -> 1 0 -> 2 1 -> 1 2
'''