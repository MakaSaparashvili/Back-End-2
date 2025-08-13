nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, nums))
squared = list(map(lambda x: x ** 2, nums))
filtered_odd = list(filter(lambda x: x % 2 != 0, nums))

print("Original:", nums)
print("Doubled:", doubled)
print("Squared:", squared)
print("Filtered (odd numbers):", filtered_odd)

