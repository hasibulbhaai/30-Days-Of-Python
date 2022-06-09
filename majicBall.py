import random

def getAnswer(Answer):
    if Answer ==1:
       return 'It is certain'
    elif Answer == 2:
        return 'It is decidely decidedly so'
    elif Answer == 3:
        return 'Yes'
    elif Answer == 4:
        return 'Reply hazy try again'
    elif Answer == 5:
        return 'Ask again later'
    elif Answer == 6:
        return 'Concentrate and ask again'
    elif Answer == 7:
        return 'My reply is no'
    elif Answer == 8:
        return 'Outlook not so good'
    elif Answer == 9:
        return 'Very doubtful'

r = random.randint(1 , 9)
fortune = getAnswer(r)
print(fortune)