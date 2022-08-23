import random

print("                           **   GET  **")
print("                           **   SET  **")
print("                           **   PLAY **")
print("              ------------NUMBER GUESSING GAME-------------")

leaderboard = ''
replay = True
while replay:
    number_to_guess = random.randint(1, 100)

    Player_name = input(' Hello Mention your Name: ')

    score = 5
    game_over = False
    while not game_over:
        guess = int(input('Please Enter Number Between 1 and 100: '))

        if guess < 50:
            print('--Your guess is too low.--')
            score -= 1
            print("Remaining attempt:" + str(score) + "\n sorry, Try another chance!")


        elif guess > 50:
            print('--Your guess is too high--.')
            score -= 1
            print("Remaining attempt:" + str(score) + "\n sorry, Try another chance!")

        else:
            print('HURRAY!!!, You are guess Correct!')
            score += 1
            print('You Scored ' + str(score))
            game_over = True

            print('Leaderboard')
    again = input('Would you like to play again? (YES/NO) ')
    if again == 'n':
        replay = False
