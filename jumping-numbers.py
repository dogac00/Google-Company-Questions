# Given a positive number x, print all Jumping Numbers smaller than or equal to x. 
# A number is called as a Jumping Number if all adjacent digits in it differ by 1. 
# The difference between ‘9’ and ‘0’ is not considered as 1. All single digit numbers are considered as Jumping Numbers. 
# For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

def check_jumping(x):
  x_string = str(x)

  if len(x_string) == 1:
    return True

  if len(x_string) == 2:
    return (abs(int(x_string[1]) - int(x_string[0])) == 1)
  
  for i in range(1,len(x_string)-1):
    if(abs(int(x_string[i]) - int(x_string[i-1])) != 1):
      return False
    elif(abs(int(x_string[i+1]) - int(x_string[i])) != 1):
      return False

  return True

def check_all(x):
  for i in range(0,x+1):
    if(check_jumping(i)):
      print(i, end=" ")

print(check_all(112))

# output is 0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 101
