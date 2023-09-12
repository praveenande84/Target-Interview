# Remove Duplicate Items in a List

given_list = [6, 1, 2, 3, 3, 4, 5, 5, 5]  # list(map(int, input().split()))
print(given_list)

print("----------------")

unique_items_list = []
for each_item in given_list:
    if each_item in unique_items_list:
        pass
    else:
        unique_items_list.append(each_item)


print(unique_items_list)

print("====================")




