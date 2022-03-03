#########################
### COMPLETE THE WORD ###
#########################

import random # importing the random module
from englishw import englishwords # importing the corrected english words list

words = ['fun', 'mouse', 'loose', 'lost', 'want', 'font', 'that', 'shot', 'fowl', 'bowl', 'bull', 'fool', 'know', 'lost'
         'golf', 'foolish', 'things', 'place', 'people', 'write', 'read', 'shoot', 'shot', 'foot', 'loot', 'boot', 'moon'
         'saloon', 'baloon', 'day', 'sunday', 'friday', 'sun', 'ball', 'Tuesday', 'school', 'food']
# Unused words list (Can Use if you want)

global score
score=0

global times
times = 0
print('Guessing game 1.0\nWelcome!') # Welcoming the player
in1 = input('>> ') # Asking for input from user
if in1 == 'rules': # If the user wants the rules
    print("""rules are pretty simple
\tYou have to answer the corrent letter to the word being shown
\t\tControls
- To quit (type "stop")
- To answer questions ("You can type any key on the keyboard")
- To answer command questions (You can press either capital or small letters based on  question)
- To Skip a question (Just press the return key)
- To get the rules (You Just did that :) (Just type rules))""") # Outputting the rules to the user


# Function for running the game in a number of times
def playgame(numOfTimes):
    global times # making the variable times global
    global score # making the variable score global
    for i in englishwords: # Going through the list of words in englishwords 
        amount = 0 
        for l in list(i): # Going through the number of letters in the words
            amount+=1 # Adding a value of 1 to form the amount of words in englishwords
            f = random.randint(0, amount-1) # Picking a random letter to be chosen as hidden
        hidden = list(i)[f] # trying to randomly pick a particular
        i = i.replace(hidden, '_') # replacing the letters with an underscore to hide it

        print(f'[WORD] {i}') # Outputing the words
        win = input('what is the missing letter marked (_) in the word? ') # Asking the user for input
        if 'stop' == win: # detecting if win equals stop and if so it will break the loop  
            break # breaking the loop
        if win == hidden: # detecting if the letter the user entered is the hidden letter/letters
            englishwords.remove(i.replace('_', win)) # removing the word from the list to avoid repetition
            print('you won, hurray!! ') # outputting when what the user typed is true
            score+=5 # Adding 5 points when the user won
            if times == numOfTimes: # if times is equal to numOfTimes
                break # stop the loop
            times+=1 # Adding 1 to the number of times the user won
        elif win == '': # detecting if the user didn't type  anything
            print('Skipping... (0 Points For that)') # printing a string
        else: # if not
            print(f'you lost :(, The Correct answer is "{hidden}" as in {i.replace("_", hidden)}') # prints string
            times-=1 # removing 1 because the user isn't correct

playgame(4) # Starts the game with numOfTimes
good = f'you scored {score} points, Great Job'
excellent = f'you scored {score} points, Excellent! '
poor = f'you scored {score} points, But you can still do better'

if score < 10: # If the score is less than 10
    print(poor) # prints out the variable poor
elif score  < 30: # If also less than 30
    print(good) # That is good
elif score > 80: # But if greater than 80
    print(excellent) # That is excellent

pf = input('Do You want to see your results?[Y/N] ') # Asking if the user wants to see results
if pf == 'Y': # If yes
   print(f'''\nYou scored: {times} Questions
Total Score: {score}points''') # output this
   if score > 0: # if score has a value greater than 0
        print(f'Question answered: [{score} Questions answered]\n') # Prints out this

if pf == 'N': # if the pf input is N
    pass # skip
else: # if not that
    ft = input('Do you want to start over again? ') # Asking for user input
    if ft == 'y': # if yes
        print('Sorry, cant repeat again')
        pass # skip
    elif ft == 'n': # if no
        print('Bye! :)')
        pass #skip

