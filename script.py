def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]

nums = [1, 2, 3, 4, 5]


def double(x):
    return x * 2

def square(x):
    return x ** 2

def is_odd(x):
    return x % 2 != 0


doubled = apply_operation(nums, double)
squared = apply_operation(nums, square)
filtered_odd = list(filter(is_odd, nums))

print("Original:", nums)
print("Doubled:", doubled)
print("Squared:", squared)
print("Filtered (odd numbers):", filtered_odd)
