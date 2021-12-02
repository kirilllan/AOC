import re
def depth_forward(arr):
  height = 0
  width = 0
  for i in range(0, len(arr)):
    end_num = re.search(r'\d+$', arr[i]).group(0)
    if arr[i][:2] == 'up': height -= int(end_num)
    if arr[i][:4] == 'down': height += int(end_num)
    if arr[i][:7] == 'forward': width += int(end_num)
  print(height * width)

depth_forward(data)
#5443732 too high #-1947824 not right answer
#1947824 right answer , was about += -= in up/down, didnt take time but took ~20 mins, woke up recently so..


import re
def depth_forward2(arr):
  height = 0
  width = 0
  aim = 0
  depth = 0
  for i in range(0, len(arr)):
    end_num = re.search(r'\d+$', arr[i]).group(0)
    if arr[i][:2] == 'up': aim -= int(end_num)
    if arr[i][:4] == 'down': aim += int(end_num)
    if arr[i][:7] == 'forward': 
      width += int(end_num)
      depth += aim * int(end_num)
  print(depth * width)

depth_forward2(data)
#1813062561, right answer, took 3 min
