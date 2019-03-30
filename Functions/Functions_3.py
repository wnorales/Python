def example3(age):
    if age > 40:
        print('You can get in')
    elif age < 40:
        print("Sorry you cannot get in")
print('Please enter your age')
Age = int(input())

example3(Age)

"""Comments"""
# We have int in front of input to convert the input into an integer. If not it will be read in as a string
# In this example we mix a function with an if else to throw some logic into the mix