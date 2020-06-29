import random
import pyfiglet 
ascii_banner = pyfiglet.figlet_format("Guess Me!!")
print(ascii_banner)  
print("Number guessing game \n")   
number = random.randint(1, 9)  
chances = 0
while chances < 5: 
    guess = int(input("Guess a number (between 1 and 9):")) 
    if guess == number: 
        print("Congratulation YOU WON!!!") 
        won = pyfiglet.figlet_format("You Won!! :)")
        print(won)
        break
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess)            
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
    chances += 1 
if not chances < 5: 
    print("YOU LOSE!!! The number is", number)
    lose = pyfiglet.figlet_format("You Lose!! ;(") 
    print(lose)
