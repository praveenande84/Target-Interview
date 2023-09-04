# Factorial

# Functions
def findFactorial(num):
    if num <= 1:
        return num
    else:
        result = num * findFactorial(num-1)
    return result


given_number = 5  # int(input())
print(given_number)

print("---------------")

factorial = findFactorial(given_number)
print(factorial)

print("=====================")