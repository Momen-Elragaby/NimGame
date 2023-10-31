"""
Name: <Momen Elragaby>

Purpose: This code simulates a game of NIM. It creates an instance of a Game class
        and allows the user to specify the number of players and the number of
        heaps. The run_game function simulates the turns for each player, and
        the take_turn function asks the user for a valid heap number and amount
        to remove from the heap. When the game is over, the function
        print_round_winner prints the winner of the round and the function
        print_player_scores prints the scores for each player.
        The user can choose to play another round by entering True when prompted,
        or end the game by entering False.

Input:   The input for this code is the number of players and the number of heaps
        for the game of NIM. The user is asked to enter these values as integers.
        The user also has the option to enter True or False when prompted to
        play another round of the game.

Output:  The output for this code is the current heap sizes and the player scores
        for each round of the game. The winner of each round is also printed.

"""


from distutils.util import strtobool

from student.game import Game
from student.heap import Heap
from student.player import Player


def main():
    """"""
    # assumes valid input
    number_of_players = int(input("Enter the number of players: "))

    # assumes valid input
    number_of_heaps = int(input("Enter the number of heaps: "))

    # Create an instance of a game class
    game = Game()

    add_players(number_of_players, game)
    add_heaps(number_of_heaps, game)

    # Call run_game
    run_game(game)



def run_game(game):
    """
    Prints the current heaps
    While the game is not over, take turns
    Once the game is over, print the round winner and player scores.
    :param game: Current game object
    :type
    :return: None
    """
    game.print_heaps()
    while not game.is_game_over():
        take_turn(game)

    game.print_round_winner()
    game.print_player_scores()

    if game.get_number_of_heaps() != 1:

        boolean_string = input('Do you want to play another round? '
                               'True or False: ')

        if boolean_string.isdigit():

            number = int(boolean_string)

            number = number % 2
            if number == 0:
                user_continue = 0
            elif number != 0:
                game.reset()
                run_game(game)
        else:
            user_continue = strtobool(boolean_string)

            if user_continue:
                game.reset()
                run_game(game)


def take_turn(game):
    """
    This function simulates the turns for a player
    :param game: current game
    :type: Game object
    :return: None
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    heap_index, amount = get_heap_amount(game)

    print_move(current_player_name, amount, heap_index)

    # update heap - currently ignoring the value returned
    game.update_heap(heap_index, amount)
    game.print_heaps()

    # increment turn if game is not over, otherwise increment current
    # player's score
    if not game.is_game_over():
        game.increment_turn()
    else:
        game.increment_player_score(turn_index)


def get_heap_amount(game):
    """
    Asks the user for a valid heap number and an amount to remove from the heap.
    :param game: current game
    :type: Game object
    :return heap_index
    :rtype int
    :return amount
    :rtype int
    """
    turn_index = game.turn_index
    current_player = game.get_player(turn_index)
    current_player_name = current_player.name

    valid_index = False
    heap_index = -1
    valid_amount = False
    amount = -1

    while not valid_amount:
        while not valid_index:
            heap_index = int(input(current_player_name
                                   + ": Choose a heap number: ")) - 1
            if heap_index < 0 or heap_index >= game.get_number_of_heaps() \
                    or game.is_heap_empty(heap_index):
                print(str(heap_index + 1) + ' is not a valid heap number.')
            else:
                valid_index = True

        amount = int(input(current_player_name +
                           ": Choose an amount to remove from heap "
                           + str(heap_index + 1) + ": "))
        if not game.is_amount_valid(heap_index, amount):
            print(str(amount) + ' is not a valid heap amount.')
            valid_index = False
        else:
            valid_amount = True
    return heap_index, amount


def add_players(number_of_players, game):
    """
    Creates the player objects and adds the player names to the game
    :param number_of_players: number of players in the game
    :type: int
    :param game: current game
    :type: Game object
    :return: None
    """
    for i in range(number_of_players):
        player_name = input("Enter a name for player " + str(i + 1) + ": ")
        player = Player(player_name)
        game.add_player(player)


def add_heaps(number_of_heaps, game):
    """
    Creates the heap objects and adds them to the game
    :param number_of_heaps: number of heaps in the game
    :type: int
    :param game: current game
    :type: Game object
    :return: None
    """
    for i in range(number_of_heaps):
        heap_size = int(input("Enter a size for heap " + str(i + 1) + ": "))
        heap = Heap(heap_size)
        game.add_heap(heap)


def print_move(player_name, amount, heap_index):
    """
    Prints the player's move
    :param player_name: name of the current player
    :type: str
    :param amount: amount of objects removed from the heap
    :type: int
    :param heap_index: index of the heap in the list of heaps
    :type: int
    :return: None
    """
    print(player_name + " takes " + str(amount) + " from heap"
          + " " + str(heap_index + 1))


if __name__ == '__main__':
    main()
