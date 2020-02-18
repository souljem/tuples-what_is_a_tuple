import math
import random
from collections import Counter
import numpy as np
#hello
'''
text = "number please"
n = int(input(text))
print (type(n))
#nn = n / 2
#print(type(nn))
'''
def is_prime(n):
  if n == 2 or n == 3 or n == 5 or n == 7:
      print("PRIME")
      return n
      pass
  t = 1
  tots = []
  next = False

  while t <= n:
    if n/t == 1 or n/t == n:
      tots.append(t)
      t += 1
    
    else:
      
      t += 1

  #print(tots)
  if len(tots) > 2 or tots[0] != 1:
    print("W")
  else:
    print("PRIME", n, tots)
    next = True

    return n, next

def next_prime(g):
  h = g /2


''''
  nn = n / 2
  print(type(nn))

  print(nn % 2) 

 

  if isinstance(nn, float) and nn % 2 < 1:
    print (" prime")
    return n
  else: 
    print("that  is not prime")
'''
def next_prime(c, b):
 
 '''
  d = c + 1
  check = is_prime(d)
  if next == True:
    print ("yessss")
  else:
'''
 '''
  t = 1
  v = []
  final = 0
  done = False
  while done == False:
    while  t <= d:
      if d/t == 1 or d/t == d:
        v.append(v)
        print(t)
        t += 1
      else:
        t += 1
        print(t)

    if len(v) > 2 or v[0] != 1:
      print("farts")
    else:
      print("PRIME", n)
      final = d
      done = True
      return final
      break
'''      
      
def addup(v):
  v += 1
  return v      
#is_prime(n)
#next_prime(n)
#print(next_prime(7))

def accumulator(x):
    i = 0
    y = 0
    z = []
    while i < x:
      y += i
      z.append(y)
      print ( z )
        
      i+= 1
        
        

    return y, z
#accumulator(10)
#print(accumulator(10))
'''
names = ["Sarina", "James", "Diana", "Rob"]
print(sorted(names, key=lambda s: s[2]))
'''

one = ("dolpins", "Marino")
two = ("49ers", "Kapernick")
three = ("colts", "Mannning")
four = ("patriots", "Brady")

fruit_dict = {'apple': 20, 'peach':15, 'pineapple':3}

# # can extract the items into a list
# #   note that the list() casting here is not necessary
# fruit_tup_list = sorted(list(fruit_dict.items()))

# for fruit in fruit_tup_list:
#     print(fruit[0], fruit[1])

#for k, v in sorted(fruit_dict.items()): 
    #print(k,v)

for key in fruit_dict: # note the .key() function is implied
  print(key, fruit_dict[key])

a = {0,1,1,2,3,5,8}
b = {3,5,8,13,21,34}

print(a.difference(b).union(b))
def set_accumulator(n):
    final = set()
    i = 0
    for i in n:
            
        final.add(i)
        
    return final

def set_accumulator(n):
  final = set()
  i = 0
  while i <= n:
    final.add(i)
    i += 1
        
  return final
print(set_accumulator(10))
a = [1, 2, 3]
b = [1, 2, 3]
i = 0
new = []
for c in a:
  print(i)
  print(c)
  new.append(((c - b[i]) ** 2))
  
  print(c, b[i])
  i += 1
print(new)
x = [4, 8, 2, 3]
y = [8, 16, 4, 6]
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)
#print(sum(a))
def euc_norm(list1, list2):
    x = float(sum(list1))
    y = float(sum(list2))
    z = math.sqrt(x + y)
    
    return z
k = 3
new_k = k
n = 5
new_n = n
i = 1
tot_n = n
while i < n:
  #print(tot_n, " multiplied BY ", (n - 1))

  tot_n = tot_n * (n - 1)
  print(tot_n)
  n -= 1
print ("combinations: ", tot_n)

tot_k = k
while i < k:
  tot_k = tot_k * (k - 1)
  print(tot_k)
  k -= 1

denominator = new_n - new_k
print(new_n, new_k, denominator)
tot_denom = denominator

while i < denominator:
  #print(tot_k, " multiplied BY ", (denominator))

  tot_denom = tot_k * (denominator)
  print(tot_denom)
  denominator -= 1

  result = tot_n / tot_denom
  print(result)

t = 5
resultss = random.randint(0, t)
print(resultss)


stw = "there's  soup soup soup soup food food that has"
stw = stw.strip()
#print(stw)
stw = stw.lower()
stw = stw.replace(".", "")
stw = stw.replace("'s", "s")
#print(stw)

r = stw.split()
u = Counter(r)
high = 0
most5 = []
keyList = {}
high = max(u, key = lambda k: u[k])
highh = max(list(u.values()))


print ("new way", highh)
highval = u[high]
count = highval

for key in u:
  keyList[key] = u[key]

for key in u:
  if key in keyList and u[key] == highh :
    print(key)
    most5.append(key)
print(keyList)
print(u)

highh = max(list(u.values()))
print("new high: ", highh)
for item in keyList:
  if key in u.keys() and u[key] == highh :
    print(key)
    most5.append(key)
    keyList.remove(key)
print (most5)

sett = [89.3, 88.5, 83.2, 84.5, 87.0, 82.2, 87.5, 88.3, 87.9, 83.2, 84.2, 86.3, 86.6, 85.6, 86.5, 88.8, 87.9, 85.5, 84.4,88.0,83.9,90.0,84.7,87.8]

def five_summary(lst):
    # Sort list, find median
    sorted_lst = sorted(lst)
    med = np.median(sorted_lst)

    # If odd length, find index of median, partition data
    if len(lst) % 2 != 0:
        med_idx = (len(lst) / 2 + .5) - 1
        low_subset = sorted_lst[:int(med_idx)]
        high_subset = sorted_lst[int(med_idx + 1):]

    # If even length, find index of median, partition data
    else:
        idx1 = int(len(lst) / 2 - 1)
        idx2 = int(idx1 + 1)

        low_subset = sorted_lst[0:idx1]
        high_subset = sorted_lst[idx2:]

    # Define Q1, Q3
    q1 = np.median(low_subset)
    q3 = np.median(high_subset)

    # Return five number summary in a tuple
    return min(sorted_lst), q1, med, q3, max(sorted_lst)

print(five_summary(sett))

'''

final = [item for item, freq in u.items() if freq == highh]
high.pop()
print(highh)
'''
'''
print("high", highval)

for key in u:
  keyList.append(key)
print (keyList)

for key in keyList:
  if u[key]  == highval:
    most5.append(key)
    keyList.remove(key)

#highval -= 1
print(highval)

for key in keyList:
  for key in keyList:
    if len(most5) < 5 and u[key]  == highval:
      most5.append(key)
      keyList.remove(key)
    
  highval -= 1
      #nexthigh = max(u, key = lambda k: u[k])
      #highvalnext = u[nexthigh]
print(highval)
print("the top 5: ", most5) 
print ("remaining in keyList: ", keyList)

print(u)
'''
  
    
'''

print(keyList, most5)  
print(r)
print(u)
print("\n", most5)

print(u)
qbs = [one, two, three, four]
g = {}
for item in qbs:
  

qb4 = {
  one[0] : one[1]
  two[0] : two[1]
  three[0] : three[1]
  four[0] : four[1]]

}


    

print(qb4)
'''