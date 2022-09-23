import random

positive_replies = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes']
negative_replies = ['Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
neutral_replies = ['Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']
question_starters = ['should', 'am', 'is', 'could', 'can', 'have', 'does', 'do']

question = input('Ask me any question:')
if question_starters in question:
    print('')
else:
    print('you need to ask a yes or no question!')

def determine_result():
    final_result = ''
    type = random.choice(['positive', 'neutral', 'negative'])
    if type == 'positive':
        final_result = random.choice(positive_replies)
    elif type == 'negative':
        final_result = random.choice(negative_replies)
    else:
        final_result = random.choice(neutral_replies)

    return final_result 

print(determine_result())