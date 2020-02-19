import math
import random
from collections import Counter
import numpy as np
'''
def num_add(x):

  sums = 0 
  temp = 0

  while x > 0:
    if x > 9:
      num_add()
      elif x >= 10 and x % 10 == 0:
        x = x/ 10
        temp = x % 10
        x = x - temp
        sums += temp

        

      elif x > 10 and x % 10 != 0:
        temp = x % 10
        x = x - temp
        sums += temp

      else:
        sums += x
        x = x - x
        sums += temp

  return sums
'''
def rec (x):
  summ = 0
  if x > 10:
    summ += x % 10
    x -= summ
    return x
  else:
     x = rec(x)
  return summ
#print(rec(191))


def t(x):
  print(x)
  if x < 1:
    return 0
  elif x % 10 + t(x // 10) > 10:
    return ((x % 10 + t(x // 10)) % 10) + (x % 10 + t(x // 10))//10
  else:
    #return x 
    return x % 10 + t(x // 10) 
  
def rangey (low, high):
  result = {}
  for x in range(low, high):
    temp = t(x)
    if result.keys() == temp:
      print("nope")
    


print(t(494))
#rangey(191, 199)
#print(t(24))

'''
num = int(191)
su = 0
if num <=0:
  return su
else:
  d = num%10
  return  num + num%10) num//10
  su += d
print(su)
'''