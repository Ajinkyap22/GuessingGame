import random
num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# create list to store player guesses
guesses = [0]

while True:
    
    guess = int(input('Enter your guess: '))
    
    if guess not in range(1,101):
        print('Out of Bounds!')
        continue

    # compare the player's guess to our number
    if guess == num:
        print(f'Correct guess! YOU WON in only {len(guesses)} turns!')
        break

    # if guess is incorrect, add guess to the list    
    guesses.append(guess)
    
    
    if guesses[-2]:
        
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')