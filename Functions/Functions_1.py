import random
def hello():
     print('Howdy!')
     print('Howdy!!!')
     print('Hello there.')
hello()



def getanswer(answernumber):
    if answernumber == 1:
     return 'It is certain'
    elif answernumber == 2:
     return 'It is decidedly so'
    elif answernumber == 3:
     return 'Yes'
    elif answernumber == 4:
     return 'Reply hazy try again'
    elif answernumber == 5:
      return 'Ask again later'
    elif answernumber == 6:
      return 'Concentrate and ask again'
    elif answernumber == 7:
      return 'My reply is no'
    elif answernumber == 8:
      return 'Outlook not so good'
    elif answernumber == 9:
      return 'Very doubtful'

r = random.randint(1, 9)  #This will select a random number from 1-9
fortune = getanswer(r)  #This will give answerNumber the value of a random number.
print(fortune)  #This will print whatever options is selected

