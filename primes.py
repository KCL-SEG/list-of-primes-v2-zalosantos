"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    semiList =[]
    n = len(list)
    i = 1
    x = 1
    if(number_of_primes>0):
        while n < number_of_primes:
            semiList.clear()
            i=1
            while i<=x:
              if x % i== 0:
                 semiList.append(i)
                 i= i+1

              else :
                 i=i+1
            if len(semiList) == 2:
                list.append(x)
                n= n+1
            else:
                i=1
            x=x+1
    else:
        raise ValueError



    return list
