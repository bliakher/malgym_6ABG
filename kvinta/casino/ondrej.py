# -------------------- imports --------------------
import random as rnd
import time as t
from typing import Optional, Callable

# -------------------- data --------------------
coin_dict = {
    True: 'head',
    False: 'tail',
    None: 'side'
}
coin_weights = (100, 100, 1)  # head, tail, side
coin_min_bet = 50  # minimal bet for coin flip

roulette_nums = (
    0, 32, 15, 19, 4,
    21, 2, 25, 17, 34,
    6, 27, 13, 36, 11,
    30, 8, 23, 10, 5,
    24, 16, 33, 1, 20,
    14, 31, 9, 22, 18,
    29, 7, 28, 12, 35,
    3, 26
)
roulette_colours = (  # french layout (from wikipedia)
    None, True, False, True, False,
    True, False, True, False, True,
    False, True, False, True, False,
    True, False, True, False, True,
    False, True, False, True, False,
    True, False, True, False, True,
    False, True, False, True, False,
    True, False
)


roulette_min_bet = 100

print_messages = {
    'main_intro': '----------------------------------------'
                  '\nInstructions:'
                  '\n- Select a game to play'
                  '\n- Place your bet (minimal money required is stated)'
                  '\n- Play the game'
                  '\n- If you win half of your bet will be added to your balance'
                  '\n- If you lose your bet will be subtracted from your balance'
                  '\n----------------------------------------',
    'main_games': 'Money: ${0}'
                  '\n- Choose an action:'
                  '\n- Exit:      [exit/e]'
                  '\n- Coin flip: [coin/c] (minimal bet: $50)'
                  '\n- Roulette:  [roulette/r] (minimal bet: $100)',
    'bet_intro': 'Set an amount of money you want to bet'
                 '\nType \'exit\' or \'e\' to leave'
                 '\nMoney: ${0}',
    'coin_intro': '--------------------'
                  '\nChoose a side on which the coin lands'
                  '\nHead: [head/h]'
                  '\nTail: [tail/t]'
                  '\nExit: [exit/e]',
    'roulette_intro': '--------------------'
                      '\nChoose a way to bet'
                      '\nColour:   [colour/c]'
                      '\nNumber:   [number/n]'
                      '\nOdd/Even: [oddeven/o]'
                      '\nExit:     [exit/e]',
    'roulette_colour': '--------------------'
                       '\nRed:   [red/r]   (odd number)'
                       '\nBlack: [black/b] (even number)'
                       '\nExit:  [exit/e]',
    'roulette_number': '--------------------'
                       '\nExit:   [exit/e]'
                       '\nNumber: [0-36]',
    'roulette_oddeven': '--------------------'
                        '\nExit: [exit/e]'
                        '\nOdd:  [odd/o]'
                        '\nEven: [even/e]'
}


# -------------------- helper functions --------------------
def place_bet(money: int, min_amt: int = 0) -> Optional[int]:
    """
    Function for getting the amount of money bet

    :param money: The amount of money a user has
    :param min_amt: Minimal amount of money required for the bet
    :return:
        None - if the user wants to quit
        int - amount of money bet
    """

    print(print_messages['bet_intro'].format(money))  # I could remove this code, could be interesting how the players would react
    print(money)
    while True:
        try:
            bet_inp = input('Amount: ').strip().lower()

            if bet_inp in ('exit', 'e'):
                return
            amt = int(float(bet_inp))  # float is there to allow float input (otherwise raises an error)

            if amt < 1:  # completely redundant, but it makes sense
                txt = 'You must bet at least some money'
            elif amt < min_amt:
                txt = f'Too little bet. You must bet at least {min_amt}'
            elif amt > money:
                txt = 'Not enough money in bank'
            else:  # if there was no error
                return amt

            # print the error
            print(txt)

        except ValueError:  # if anything goes wrong
            pass


def game_result(money: int, bet: Optional[int], game: Callable[[], Optional[bool]]) -> tuple[int, bool]:
    """
    Function for finalising game's result.

    :param game: game user wants to play
        - this method of choosing a game proved to be better since it doesn't repeat code
    :param money: user's money before playing the game
    :param bet: user's bet
    :return: user's money after playing the game and whether they want to exit
    """
    if bet is None:  # if the user exits bet placing
        print('----------------------------------------')
        return money, True

    result = game()
    if result is None:  # if the user exits/doesn't have enough money
        print('----------------------------------------')
        return money, True
    elif result:
        print('You won!')
        money += int(0.5 * bet)
    else:
        print('You lost.')
        money -= bet

    print('----------------------------------------')
    t.sleep(1)
    return money, False


def play_game(money: int, min_bet: int, game: Callable[[], bool]) -> int:
    end = False
    while not end:
        if money < min_bet:
            print('Not enough money for selected game'
                  '\n----------------------------------------')
            break
        money, end = game_result(money, place_bet(money, min_bet), game)

    if money > 0:
        print(print_messages['main_games'].format(money))
    return money


# -------------------- games --------------------
def coin() -> Optional[bool]:
    """
    Flips a coin.
    The coin can either land on head, tail or side.

    :return: result of the game or None if user wants to exit
    """

    # ----- intro -----
    print(print_messages['coin_intro'])
    while True:
        inp = input('Action: ').lower().strip()
        # ----- options -----
        if inp in ('exit', 'e'):
            return
        elif inp in ('head', 'h'):
            guess = True
        elif inp in ('tail', 't'):
            guess = False
        elif inp in ('side', 's'):
            guess = None
        else:
            print('Unknown option, try again please')
            continue
        break
    print('--------------------')

    # ----- coin flip -----
    res = rnd.choices((True, False, None), coin_weights, k=1)[0]
    # ----- additional rig -----
    if guess == res and not rnd.randint(0, 16):
        res = not res

    # ----- result -----
    print(f'The coin landed on {coin_dict[res]}!')
    return guess == res


def roulette() -> Optional[bool]:
    """
    Roulette game
    There are 3 modes a user can choose:
    - colour
    - odd/even
    - exact number

    :return: result of the game or None if user wants to exit
    """
    # ----- intro -----
    print(print_messages['roulette_intro'])
    while True:
        inp = input('Action: ').lower().strip()
        # ----- bet options -----
        if inp in ('exit', 'e'):
            return
        elif inp in ('colour', 'c'):
            game_choice = True
        elif inp in ('number', 'n'):
            game_choice = False
        elif inp in ('odd/even', 'o'):
            game_choice = None
        else:
            print('Unknown option, try again please')
            continue
        break

    # ----- guess options -----
    if game_choice is None:  # bet on odd/even
        print(print_messages['roulette_oddeven'])
        while True:
            inp = input('Action: ').lower().strip()
            # ----- options -----
            if inp in ('exit', 'e'):
                return
            elif inp in ('odd', 'o'):
                guess = True
            elif inp in ('even', 'v'):
                guess = False
            else:
                print('Unknown option, try again please')
                continue
            break
    elif game_choice:  # bet on colour
        print(print_messages['roulette_colour'])
        while True:
            inp = input('Action: ').lower().strip()
            # ----- options -----
            if inp in ('exit', 'e'):
                return
            elif inp in ('red', 'r'):
                guess = True
            elif inp in ('black', 'b'):
                guess = False
            else:
                print('Unknown option, try again please')
                continue
            break
    else:  # bet on number
        print(print_messages['roulette_number'])
        while True:
            inp = input('Action: ').lower().strip()
            # ----- options -----
            if inp in ('exit', 'e'):  # if user wants to exit the game
                return

            elif not inp.isdigit():  # if the input cannot be converted into a number
                print('Unknown option, try again please')
                continue

            guess = int(inp)
            if not (0 <= guess <= 36):
                print('Number is not between 0 and 36')
                continue

            break  # if a valid number was chosen

    # ----- number generation -----
    for _ in range(10):  # prints random number 10 times, them proceeds
        t.sleep(0.2)
        print(rnd.choice(roulette_nums), end='')
        t.sleep(0.2)
        print('.', end='')
        t.sleep(0.2)
        print('.', end='')
    t.sleep(1)

    number = rnd.choice(roulette_nums)
    print(f'\nThe ball landed on {number}'
          f' ({"red" if roulette_colours[roulette_nums.index(number)] else "black"})!')

    if game_choice is None:  # odd/even bet
        return number % 2 == int(guess)
    elif game_choice:  # colour bet
        return roulette_colours[roulette_nums.index(number)] == int(guess)
    else:  # number bet
        return guess == number


# -------------------- main program --------------------
if __name__ == '__main__':
    balance = 1000

    # ----- intro -----
    print(print_messages['main_intro'])
    # ----- option selection -----
    print(print_messages['main_games'].format(balance))
    while balance > 0:
        end_game = False
        # ----- input -----
        inp = input('Action: ').lower().strip()
        # ----- game to play / exit the game -----
        if inp in ('exit', 'e'):  # if the user wants to exit
            print('--------------------'
                  f'\nYour balance is ${balance}')
            break
        elif inp in ('coin', 'c'):  # if the user wants to flip a coin
            game = coin
        elif inp in ('roulette', 'r'):  # if the user wants to play roulette
            game = roulette
        else:
            print('Unknown option, try again please')
            continue

        # ----- playing the game -----
        balance = play_game(balance, coin_min_bet, game)
    else:
        print('You have run out of money!')

    print('\nThanks for your visit, come again!')
