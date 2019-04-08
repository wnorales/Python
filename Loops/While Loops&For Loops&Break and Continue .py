# There are two types of loops in python for and while loops
#For Loops
Prime_Numbers = [2, 4, 6, 8, 10, 12]
Odd_Numbers = [1, 3, 5, 7, 9, 11]

for x in Prime_Numbers:
    print("Your prime number is " + str(x))
for y in Odd_Numbers:
    print("Your odd number is " + str(y))
# While Loops need a condition to test
number = 1
count = 12
while count > number:
    print('Good job ' + str(number))
    number += 2
if number > count:
    print("Great job")
    print("200")
#Break this will brake the loop at a certain point
Number1 = 100
Number2 = 200

while True:
    print(Number1)
    Number1 += 5
    if Number1 >= Number2:
        break
#Continue  This will skip the number 150
for z in range(200):
    if z == 150:
        continue  # This will skip 150
    print(z)