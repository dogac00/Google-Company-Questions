# Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

# Example :

# A : [3 5 4 2]

# Output : 2 
# for the pair (3, 4)

arr = [3,5,4,2]

length = len(arr)
max_ = 0

for i in range(length):
  for j in range(i+1,length):
    if(arr[j] >= arr[i] and j - i > max_):
      max_i, max_j = i,j
      max_ = j - i

print(max_)
print("for the pair ({},{})".format(arr[max_i], arr[max_j]))
