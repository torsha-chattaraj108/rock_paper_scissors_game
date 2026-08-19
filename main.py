from engine import RockPaperScissors
while True:
    print('\n'+'='*46)
    print(' ROCK PAPER SCISSORS! TYPE "quit" TO END GAME. ')
    print('\n'+'='*46)
    try:
        num_rounds=int(input('Enter the no of rounds you want: '))
    except ValueError:
        print('That was not a number. Setting rounds as 3.')
        num_rounds=3
    game=RockPaperScissors(num_rounds)
    game()
    again=input('\nDo you want to play again? (yes/no): ').lower().strip()
    if again not in ['yes','y']:
        print('Thanks for playing. GOODBYE!')
        break
