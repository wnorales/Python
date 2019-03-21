def hello():
     print('Howdy!')
     print('Howdy!!!')
     print('Hello there.')
hello()
hello()
hello()



import random
def getAnswer(answerNumber):
    if answerNumber == 1:
     return 'It is certain'
    elif answerNumber == 2:
     return 'It is decidedly so'
    elif answerNumber == 3:
     return 'Yes'
    elif answerNumber == 4:
     return 'Reply hazy try again'
    elif answerNumber == 5:
      return 'Ask again later'
    elif answerNumber == 6:
      return 'Concentrate and ask again'
    elif answerNumber == 7:
      return 'My reply is no'
    elif answerNumber == 8:
      return 'Outlook not so good'
    elif answerNumber == 9:
      return 'Very doubtful'

r = random.randint(1, 9) #This will select a random number from 1-9
fortune = getAnswer(r) #This will give  answerNumber the value of a random number.
print(fortune) #This will print whatever options is selected

