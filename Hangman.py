game_running = True

while game_running:
    print()
    print('Im thinking of a word, do you think you can guess it?')

# Have the program have a random set of words to chose from

Word = 'Will'

# Word2 = 'Great'
# Word3 = "Today"

Word4 = 'Never'

while Word4 != Word:

      # Get the player's guess from the player

    print()
    guess = input('Please enter a word:')

    # Does the user want to quit playing?

    if guess == 'quit':
        game_running = False
        break
    else:

        # Otherwise, nope, player wants to keep going
        # Convert the players guess from a string to an integer

        Word4 = str(guess)

    if Word4 == Word:
        print()
        print('Good Job Will')
    else:

        # Otherwise, whoops, nope, go around again

        print()
        print("Oh, to bad, that's not my word...")

