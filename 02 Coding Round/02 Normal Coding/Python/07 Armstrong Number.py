# Armstrong Number

given_number = "153"  # input()
print(given_number)

print("-------------------")

power = len(given_number)

is_armstrong = False

result = 0
for each_number in given_number:
    add_value = int(each_number) ** power
    result += add_value

if result == int(given_number):
    is_armstrong = True


print(is_armstrong)

print("=======================")

