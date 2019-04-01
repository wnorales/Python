import random
Person1 = ['Rock', 'Paper', 'Scissors']
Person2 = ['Rock', 'Paper', 'Scissors']
Person1_Random = (random.choice(Person1))
Person2_Random = (random.choice(Person2))

print(Person1_Random)
print(Person2_Random)

def result(Person1, Person2):
    if Person1 == "Rock" and Person2 == "Scissors":
        print('Person 1 wins')
    elif Person1 == "Paper" and Person2 == "Rock":
        print('Person 1 wins')
    elif Person1 == "Scissors" and Person2 == "Paper":
        print('Person 1 wins')
    elif Person2 == "Rock" and Person1 == "Scissors":
        print('Person 2 wins')
    elif Person2 == "Paper" and Person1 == "Rock":
        print('Person 2 wins')
    elif Person2 == "Scissors" and Person1 == "Paper":
        print('Person 2 wins')


if Person1_Random == Person2_Random:
    print('Nope go again')
elif Person1_Random != Person2_Random:
    result(Person1_Random, Person2_Random)

"""Comments"""
# The above function is ran unless its hits the elif. The elif decides what the output is.