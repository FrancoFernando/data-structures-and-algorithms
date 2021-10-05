import math 
from typing import List

def IsPrimeBruteForce (n : int) -> bool:

    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def IsPrime(n : int) -> bool:

  if n == 2:
      return True
  if n <= 1 or n % 2 == 0:
      return False
  
  m = int(math.sqrt(n))

  for i in range(3,m,2):
        if n % i == 0:
            return False

  return True
  
def Sieve(n : int) -> List[bool]:

  prime = [True] * (n+1)
  prime[0] = False
  prime[1] = False

  m = int(math.sqrt(n))

  for i in range(2,m+1):
      if prime[i]:
        for j in range(i**2,n+1,i):
            prime[j] = False
            
  return prime