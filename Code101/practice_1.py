# count = 0
#
# for i in range(0, 1000):
#     if i%3 == 0 or i%5 == 0:
#         count += i
#         print(count)


#fibonacci sequence! taking all the numbers that are even and summing them up.

# def fib(max):
#     f1, f2, = 0, 1
#     while f1 < max:
#         yield f1
#         f1, f2 = f2, f1 + f2
# print(sum(filter(lambda n: n % 2 == 0, fib(4000000))))


# #Largest prime factor
# n = int(input('Enter Range Int: '))
# primes = []
# largePrime = []
# for i in range(2, n):
#     #assume number is prime until show it is not.
#     isPrime = True
#     for num in range(2, i):
#         if i % num == 0:
#             isPrime = False
#     if isPrime:
#         primes.append(i)
# for x in primes:
#     if n%x ==0:
#         largePrime.append(x)
#
# print(largePrime)



n = 600851475143
i = 2
while i * i <= n:
    while n%i == 0:
        n=n/i
    i = i +1
print(n)
