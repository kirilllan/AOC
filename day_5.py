ary = [['0,95,9'],['8,00,8'],['9,43,4'],['2,22,1'],['7,07,4'],['6,42,0'],['0,92,9'],['3,41,4'],['0,08,8'],['5,58,2']]


def day5(arr):
  points_grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,],[-1,-1,-1,-1,-1,-1,-1,-1,-1,]]
  for i in range(0, len(ary)):
    xy1 = ''.join(arr[i])[:3].rstrip(',')
    xy2 = ''.join(arr[i])[3:6].rstrip(',')
    x1 = int(xy1[0])
    y1 = int(xy1[-1])
    x2 = int(xy2[0])
    y2 = int(xy2[-1])
    # yrange = range(min(y1, y2))
    # print(yrange)
    for ii in range(min(y1, y2), max(y1, y2)):
      for iii in range(min(x1, x2), max(x1, x2)):
        points_grid[ii][iii] += 1

  print(points_grid) 

#day5(ary)




### took too much time for me. not interested in completing. answer from web:
import numpy as np

grid = np.zeros((2, 1000, 1000))
print(grid)
exit()
ls = np.fromregex(open(0), '\d+', [('',int)]*4)

for (x, y, X, Y) in ls:
    dx, dy = np.sign([X-x, Y-y])                 
    while (x,y) != (X+dx, Y+dy):
        grid[dx * dy, x, y] += 1
        x+=dx; y+=dy

print((grid[0]>1).sum(), (grid.sum(0)>1).sum())
#The grid[dx*dy,x,y] trick works because dx*dy is 0 for a horizontal or vertical line, and -1 or +1 for a diagonal.