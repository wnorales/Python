my_list = [10, 12, 23, 44, 77, 89, 122]

for n in range(300):  # This will just print every number from 0 to 300
    if n in my_list:  # This will only print the numbers from the my_list section
        print(n)

for f in range(300):  # This will just print every number from 0 to 300
        if f == my_list:  # This will be the  value to be skipped
            continue  # This will bypass the 295 number
        print(f)      # This will print the list


for x in list(range(1, 13)) + list(range(15, 400)):  # This will just print every number from 0 to 400 excluding the number 14
    if x in my_list:  # This will check the values in the my_list
        x += 2        # This will add 2 to each value
        print(x)
    if x == 14:
        print('There is the magic number')