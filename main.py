import math
import random
from collections import Counter
import numpy as np
#print(2**-3)
def sigmoid (x):
  result = 1/(1 + (2.71828**-x))
  return result


print(sigmoid(3))