
from math import gcd

#no. of bead positions, no. of colours of bead, sum placeholder
n = 5
r = 5
sum = 0
# list of divisors of n to be appended
divisors = []

# euler's totient function 
def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

# appending divisors < n to list
for x in range (1,n):
    if n%x==0:
        divisors.append(x)     

# appending n to this list also
divisors.append(n)
# for divisor in list
for k in divisors: 
    # calculate as in formula
    sum += phi(k)*r**(n/k)

# divide sum by n as in formula
h = 1/n * sum 
# print configuration count   
print(int(h))
