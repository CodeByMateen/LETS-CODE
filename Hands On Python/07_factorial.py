import math

n = 5
fact = 1
j = n

# using for loop
# for i in range(n, 0, -1):
#     fact *= i

while(j >= 1):
    fact *= j
    j-=1
    
print(fact)
print(math.factorial(6))
