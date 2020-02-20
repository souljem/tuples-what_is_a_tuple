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
def rec_dig_sum(x):
  #print(x)
  if x < 1:
    return 0  
  else:
    #return x 
    return x % 10 + t(x // 10)
  
def distr_of_rec_digit_sums (low, high):
  temp = 0
  result = {}
  values = []
  for x in range(low, high):
    result[rec_dig_sum(x)] = 1
    values.append(rec_dig_sum(x))
  #print("all the values\n ", values)
  #print("first dictionary\n" , result, "\n")

  #print("top", max(values))
  #START HERE !!!!!
  #max_values = max(values)
  for x in values:
    if x > 10:
      result[rec_dig_sum(x)] += 1
      result[x] -= 1
      #print( x, " should be one higher")
    
      #print(x, " Is less than 10")
  
    

  for u in list(result):
    #print("bortols! ", u)
    #print("the value of ", u, " is ", result[u])
    if u > 10:
      result.pop(u) 
      #print("the value of ", u, " is ", result[t(u)])

      #print("new bortols ", result)
  return result
'''
''' 
'''      
      if result[u] in result.values():
        result[u] += 1
'''
  
  


#print(t(t(494)))
print(distr_of_rec_digit_sums(191, 309))
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