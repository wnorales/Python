def example(name, age, height):  # Functions should always be lower case
    print('Hello ' + name + ' Your age is ' + age + ' and you are currently ' + height)

print('What is your name?')
Name = input()
print("What is your age")
Age = input()
print("How tall are you?")
Height = input()

example(Name, Age, Height)

# In this example all we need to do is run the function example and it will take the following inputs and convert them into a sentence.