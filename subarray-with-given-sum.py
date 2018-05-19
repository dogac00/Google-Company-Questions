# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
given_sum = 15

length = len(arr)

for i in range(length):
  for j in range(i+1,length):
    if(sum(arr[i:j]) == given_sum):
      print("The sum from the index {} to the index {} is {}".format(i,j,given_sum))
