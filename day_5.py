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

day5(ary)