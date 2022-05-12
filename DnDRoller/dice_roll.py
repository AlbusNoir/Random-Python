import random, sys, time

def roll_dice(dice):
    animation = ["|", "/", "-", "\\"]
    idx = 0

    if dice in('d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'):
        dice = dice
        print(f"Rolling {dice}...")
        
        # this is literally just for flair
        for i in range(12):
            print(animation[idx % len(animation)], end='\r')
            idx += 1
            time.sleep(0.1)

        die = int(dice[1:])
        roll = random.randint(1,die)
        print(f'You rolled: {roll}\n')
    else:
        print(f'{dice} is not a die option. Try again\n')
        main()
        

    again = input("Would you like to roll again? (Yes or No?): ")
    if again.lower() == 'y':
        main()
    if again.lower() == 'n':
        print('Goodbye')
        sys.exit()


def main():
    dice = input("What would you like to roll? d4, d6, d8, d10, d12, d20, or a d100?\nRoll a: ")

    roll_dice(dice)


if __name__ == '__main__':
    diceart=r"""
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/
DnDRoller

"""
    print(diceart)
    main()