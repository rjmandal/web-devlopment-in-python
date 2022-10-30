'''Problem Statement: You have to write a Word Puzzle Game in which the user has to form
the correct word out of a given set of characters. In the game the user has to solve this
puzzle for 5 words, one at a time. Problem words are stored in a list and appear to the user
in random sequence. Give the user score +1 for each correct answer and give -1 for each
wrong answer. At last print the final score. You can store any number of words in the list, but
in each round of the game only 5 words are shown to the user.'''

import random
list=['RAEHTF','KABRE','SYAJNA','RENEG','OAERELANP','ANDALM']
list1=['father','brake','sanjay','green','aeroplane','mandal']
score=0
for e in range(5):
    print('Arrange the letters to form a valid word:')
    n=random.randint(0,5)
    print(list[n])
    ans=input()
    if ans==list1[n]: 
        print("\nCorrect\n")
        score+=1
    else:
        print('\nWrong\n')
        score-=1   

print('Net Score is ',score)