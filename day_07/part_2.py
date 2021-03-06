def dist(nums, n):
    return sum(triangle(abs(x - n)) for x in nums)

def triangle(n):
    return n*(n + 1)//2

nums = [int(n) for n in next(open('input.txt')).split(',')]

min_fuel = float('inf')
for i in range(max(nums)):
    min_fuel = min(dist(nums, i), min_fuel)

print(min_fuel)