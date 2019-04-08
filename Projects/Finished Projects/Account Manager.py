import random
First_Name = ''
Last_Name = ''
Age = ''
while True:
    print(First_Name)
    First_Name = input('Please enter a First Name \n')
    if First_Name.isalpha():
        print('Great')
        break
while True:
    print(Last_Name)
    Last_Name = input('Please enter a Last Name \n')
    if Last_Name.isalpha():
        print('Your Doing Great ')
        break
while True:
    print(Age)
    Age = input('Please enter your age \n')
    if Age.isalnum():
        print('Amazing')
        break


for x in range(1):
    A = (random.randint(4000, 4200))
    B = (random.randint(4200, 4999))
    C = (random.randint(4200, 4999))
    D = (random.randint(4200, 4999))


print('Card number is ' + str(A),  str(B),  str(C),  str(D))


for y in range(1):
    FirstPart_AccountNumber = (random.randint(100, 600))
    SecondPart_AccountNumber = (random.randint(1000, 5000))
    ThirdPart_AccountNumber = (random.randint(2500, 6000))

print('Your account number is ' + str(FirstPart_AccountNumber), str(SecondPart_AccountNumber), str(ThirdPart_AccountNumber))

print('Would you like to save your account information Yes or No\n')
Saving = input()


#Name = First_Name + ' ' + Last_Name + ' Your card numbers are ' + str(A),  str(B),  str(C),  str(D) + 'and your account number is ' + str(FirstPart_AccountNumber), str(SecondPart_AccountNumber), str(ThirdPart_AccountNumber)
#print(' Hello ' + Name)



