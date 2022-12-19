""" 
We are going to write a program that generates a random number and asks the user to guess it
1) if the players guess is higher than the actual number the program displays lower number please
2) similarly if the guess is too low it will display higher number please
3) And if userguess is equal to the random number taken by the computer , it will display you guessed it right
"""
 
# first we will import a random module 
import random
RandomNumber=random.randint(1,100) # the computer will take a random number between 1 and 5 including both
#print(RandomNumber)
print("*********WELCOME TO THE GUESS GAME*********")
guesses=0
userguess=None
while(userguess!=RandomNumber): # intoduced a while loop here which will take the input till the condition
   userguess=int(input("Please Enter your Guess below : \n"))
   guesses+=1
   if userguess==RandomNumber:
    print("You guessed it right!!!!")
   else:
    if(userguess>RandomNumber):
        print("You guessed it wrong!!!   \n Guess a smaller number")
    else:
        print("You guessed it wrong!!!   \n Guess a larger number")
        
print(f"You guessed the number in {guesses} times")

#Now A file as been created as HighScore.txt
#if the user beats the previous HighScore then the users score will be printed there

with open("HighScore.txt") as f:
    HighScore=int(f.read())
    if(guesses<HighScore):
       print("Congratulations you just broke the HighScore ")
    with open("HighScore.txt","w") as f:
     f.write(str(guesses))