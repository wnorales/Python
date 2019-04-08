List = [8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 300]

for n in range(1, 200):
    if n in List:
        print(n)
"""Example of a for loop. Prints only numbers within the list above. Does not print 300 since its not in the range from 1-200"""


MagicNumber = 60
for n in range(100):
    if n is MagicNumber:
        print("The magic number is " + str(n))