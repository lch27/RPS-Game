import random, sys

print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

        def get_user_input():
            return input()

        playerMove = get_user_input()

        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s,')

    if playerMove == 'r':
        print('Rock versus ...')
    elif playerMove == 'p':
        print('Paper versus ...')
    elif playerMove == 's':
        print('Scissors versus ...')

    randomNum = random.randint(1, 3)
    if randomNum == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNum == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNum == 3:  # Corrected from '3'
        computerMove = 's'
        print('Scissors')

    if playerMove == computerMove:
        print('It is a tie.')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses += 1
