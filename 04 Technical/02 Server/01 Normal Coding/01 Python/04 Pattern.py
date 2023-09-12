
# X-pattern

given_number = 5
print(given_number)

print("--------------------")

number_of_rows = given_number

for counter in range(0, number_of_rows):
    row = [" "] * number_of_rows
    star = "*"
    row[counter] = star
    row[-counter-1] = star
    print(*row)


print("=====================")

#  Output

'''
*   *
  *
*   *
'''





