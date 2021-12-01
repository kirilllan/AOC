def increases_amount(arr):
  count = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]: count += 1
  print(count)
  return count

#1501 is too low
#1502 was right answer, guessed it. took 15min total time
increases_amount(ary)


def three_measurement(arr):
  count = 0
  for i in range(0, len(arr)):
    p1 = arr[i:i+3]
    p2 = arr[i+1:i+4]
    #print((p1))
    if (sum(p2, 0) > sum(p1, 0)): count += 1
  print(count)
  return count

#1444 too low
#1538 was right one. took 15 min total to complete (again)
three_measurement(ary)
