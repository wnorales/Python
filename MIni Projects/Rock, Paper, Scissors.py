import random

Output = ['Rock', 'Paper', 'Scissors']

print(random.choice(Output))
if random.choice(Output) == "Rock":
    print('Good')
elif random.choice(Output) == "Paper":
    print('Great Job')
elif random.choice(Output) == "Scissors":
    print('Excellent job')