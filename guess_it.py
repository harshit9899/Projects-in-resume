import random
randNum = random.randint(1,100)
# print(randNum)
userGuess = int(input("Enter the guess"))
guessNum = 0
while (userGuess != randNum) :
    print("You guessed it wrong")
    if userGuess<randNum :
        print("Enter larger number")
    else :
        print("Enter smaller number")
    userGuess = int(input("Enter another guess"))
    guessNum += 1
print("You guessed it right")
print(f"Number of guesses used= {guessNum}")
with open ('highscore.txt','r') as f :
    hiScore = int(f.read()) 
if (guessNum<hiScore) :
    print("You have broken the highscore!")
    with open ('highscore.txt','w') as f:
        f.write(str(guessNum))