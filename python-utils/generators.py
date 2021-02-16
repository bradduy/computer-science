import sys

def calculate(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def calculateGenerator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(calculate(1000000)))
print(sys.getsizeof(calculateGenerator(1000000)))

############# FIBONNACI #############
def fibonacci(limit):
    first, second = 0, 1
    while first < limit:
        yield first
        first, second = second, first + second

fib = fibonacci(100)
for i in fib:
    print(i)


##### generator initiate ############
myGenerator = (i for i in range(10) if i% 2 == 0)
print(list(myGenerator))