import random
class RockPaperScissors:
    def __init__(self,rounds):
        self.choices=['rock','paper','scissors']
        self.counters={'rock':'paper','paper':'scissors','scissors':'rock'}
        self.total_rounds=rounds
        self.score={'you':0,'comp':0,'tie':0}
        self.streak=0
        self.rounds_played=0
        self.win_text='No rounds completed'
        self.difficulty='easy'
        self.history={'rock':0,'paper':0,'scissors':0}
    def select_difficulty(self):
        while True:
            level=input('Enter the difficulty level(easy/difficult): ').strip().lower()
            if level in ['easy','difficult']:
                self.difficulty=level
                print(f'Difficulty level set to {self.difficulty.upper()}\n')
                break
            print('Invalid selection')
    def get_choice(self):
        if self.difficulty=='easy' or self.rounds_played==0:
            return random.choice(self.choices)
        max_frequency=max(self.history.values())
        most_frequent=[move for move,count in self.history.items() if count==max_frequency]
        if len(most_frequent)>1:
            predicted_user_move=random.choice(most_frequent)
        else:
            predicted_user_move=most_frequent[0]
        return self.counters[predicted_user_move]
    def get_result(self,user,comp):
        if user==comp:
            return 'tie'
        elif (user,comp) in [('scissors','paper'),('rock','scissors'),('paper','rock')]:
            return 'won'
        else:
            return 'lost'
    def play_game(self):
        self.select_difficulty()
        for i in range(1,self.total_rounds+1):
            while True:
                user=input(f'\nEnter your choice(rock-paper-scissors): ').lower()
                if user=='quit' or user in self.choices:
                    break
                print('Invalid choice. Try again. ')
            if user=='quit':
                print('Quitting early.')
                break
            comp=self.get_choice()
            self.history[user]+=1
            print(f'You chose: {user} | I chose: {comp}')
            result=self.get_result(user,comp)
            self.rounds_played+=1
            if result=='won':
                print('You won')
                self.score['you']+=1
                self.streak=self.streak+1 if self.streak>0 else 1
            elif result=='lost':
                print('I won')
                self.score['comp']+=1
                self.streak=self.streak-1 if self.streak<0 else -1
            else:
                print('Its a tie')
                self.score['tie']+=1
                self.streak=0
            win_rate=(self.score['you']/self.rounds_played)*100
            comp_rate=(self.score['comp']/self.rounds_played)*100
            if win_rate>comp_rate:
                self.win_text=f'You won by {win_rate:.1f}%'
            elif win_rate<comp_rate:
                self.win_text=f'I won by {comp_rate:.1f}%'
            else:
                self.win_text=f'We both won'
            if self.streak>0:
                streak_text=f' {self.streak} WIN STREAK'
            elif self.streak<0:
                streak_text=f' {abs(self.streak)} LOSE STREAK'
            else:
                streak_text=f'NEUTRAL STREAK'
            print(f"Your current score: {self.score['you']}| My current score: {self.score['comp']}| Tie:{self.score['tie']}")
            print(f"Win rate: {win_rate:.1f}% | {streak_text}")
            if self.rounds_played==0:
                print('\nNo rounds were played')
                return
        print(f"\n{'FINAL STATS ':=^46}")
        print(f"Your final score: {self.score['you']:>28}")
        print(f"My final score:   {self.score['comp']:>28}")
        print(f"Tie:              {self.score['tie']:>28}")
        print(f"Outcome:          {self.win_text:>28}")
    def __call__(self):
        self.play_game()
