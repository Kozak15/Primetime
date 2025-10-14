
#O(sqrt n)
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#Sieve of Eratosthenes O(n log log n)
def sieve(n):
    if n < 2:
        return []
    else:
        sief = [2]
        ans = []
        for i in range(3 , n + 1):
            sief.append(i)
        for j in sief:
            if isprime(j) == True:
                ans.append(j)
        return ans
#Fermat pseudoprime test
#If n is prime, 2**n-2 % n == 0. But if 2**n-2 % n == 0, n is not always prime.
def pseudoprime(n):
  ans = []
  for i in range(2 , n):
    if ((2 ** i - 2) % i) == 0 and isprime(i) != True:
      ans.append(i)
  return ans
#All primes are of the form 4k+1 or 4k+3 except 2. It can also be 6k+1 or 6k-1 except 2 and 3.
#Function returns 4k+r primes count where r is 1 or 3 less than n.
def countprime(n , r):
    count = 0
    for i in range(2 , n):
        if isprime(i) == True and i % 4 == r:
            count += 1
    return count

#countprime(n,1) > countprime(n,3) first at n = 26861

#100 Bottles of beer
for i in range(100,-1,-1):
    if i == 0:
        print("Damn, we're out of beer!")
        print('Remember kids, alcohol is bad')
    else:
        print(f"{n} bottles of beer on the wall.")
        print(f"{n} bottles of beer.")
        print("Take one down, pass it around,")
        print(f"{n-1} bottles of beer on the wall\n")

