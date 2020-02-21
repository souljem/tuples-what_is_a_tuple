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
  if x < 1:
    return 0
  elif x > 9:
    return rec_dig_sum(x % 10 + rec_dig_sum(x // 10))
  else: 
    return x % 10 + rec_dig_sum(x // 10)
  
def distr_of_rec_digit_sums (low, high):
  temp = 0
  result = {}
  values = []
  for x in range(low, high):
    exists = rec_dig_sum(x)
    result[exists] = result.get(exists, 0) + 1
  print (result)
  return result


#print(distr_of_rec_digit_sums(167, 210))
print(rec_dig_sum(166))

'''    
    exists = rec_dig_sum(x)
    if exists in result.keys():
      
      print("hotel")
    else:
      #result[exists] = 1
      print("not here ")
  print("Farts",result)
'''
  

'''    
    if rec_dig_sum(x) < 10:
      result[rec_dig_sum(x)] = 1
    elif rec_dig_sum(x) >= 10:
      result[rec_dig_sum(rec_dig_sum(x))] = 1
    else:
      result[rec_dig_sum(rec_dig_sum(rec_dig_sum(x)))] = 1


  
      
      

    values.append(rec_dig_sum(x))
  print("you", len(result.keys()))
  for x in values:
    if x > 10:
      result[rec_dig_sum(x)] += 1
      
        
  for u in list(result):
    if u > 9:
      result.pop(u) 

'''
  


  


'''
''' 
'''      
      if result[u] in result.values():
        result[u] += 1
'''
  
  


#print(rec_dig_sum(167))
#print(distr_of_rec_digit_sums(167, 210))
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