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

# Tthe trick of the recursion here is actually to run the function on the function.
def t(x):
  print(x)
  if x < 1:
    return 0  
  else:
    #return x 
    return x % 10 + t(x // 10) 
  
def rangey (low, high):
  temp = 0
  result = {}
  values = []
  for x in range(low, high):
    result[t(x)] = 1
    values.append(t(x))
  print(values)
  for x in values:
    if result[x] and x < 10:
      result[x] += 1
# getting the correct amount in values 
  for u in result.keys():
    #print("bortols! ", u)
    print(result[u])
    if u > 10:
      result[t(u)] += 1

      #print("new bortols ", result)
  return result 
'''      
      if result[u] in result.values():
        result[u] += 1
'''
  
  


#print(t(t(494)))
print(rangey(191, 309))
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