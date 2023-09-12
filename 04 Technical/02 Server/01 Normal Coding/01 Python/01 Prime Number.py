# Find Prime Numbers

given_number = 10 # int(input())
print(given_number)

print("--------------------")

prime_numbers_list = []
for main_counter in range(1, given_number+1):
    factors_count = 0
    for sub_counter in range(1, main_counter+1):
        if main_counter % sub_counter == 0:
            factors_count += 1
    if factors_count == 2:
        prime_numbers_list.append(main_counter)

print(prime_numbers_list)

print("=======================")


