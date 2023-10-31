class Game:
    """
    Game class simulates a game
    author(s): Momen Elragaby
    """
    def __init__(self):
        """
        Constructor creates an empty list of heaps and an empty list of players,
        and sets the turn_index to 0.
        turn_index represents which player's turn it is.
        """
        self.__heaps = []
        self.__players = []
        self.__turn_index = 0

    @property
    def turn_index(self):
        """
        Getter method that returns the current turn_index.

        :return: The current turn_index.
        :rtype: int
        """
        return self.__turn_index

    def get_player(self, player_index):
        """
        Returns the player that is referenced by player_index
        :param player_index: the index of the player in the players list
        :type player_index: int
        :return: the player that is referenced by player_index
        :rtype: Player
        """
        return self.__players[player_index]

    def get_heap(self, heap_index):
        """
        Returns the heap that is referenced by heap_index
        :param heap_index: the index of the heap in the heaps list
        :type heap_index: int
        :return: the heap that is referenced by heap_index
        :rtype: Heap
        """
        return self.__heaps[heap_index]

    def get_number_of_heaps(self):
        """
        Returns the length of the heap list
        :return: the number of heaps in the game
        :rtype: int
        """
        return len(self.__heaps)

    def add_player(self, player):
        """
        Appends player to the end of the players list.
        :param player: the player to add to the game
        :type player: Player
        :return: None
        """
        self.__players.append(player)

    def increment_turn(self):
        """
        Increments the turn_index by 1. If the turn_index is greater than or
        equal to the number of players,
        it sets turn_index to 0.
        :return: None
        """
        self.__turn_index += 1
        if self.__turn_index >= len(self.__players):
            self.__turn_index = 0

    def add_heap(self, heap):
        """
        Appends heap to the end of the heap list.
        :param heap: the heap to add to the game
        :type heap: Heap
        :return: None
        """
        self.__heaps.append(heap)

    def update_heap(self, heap_index, amount):
        """
        Removes amount from the heap at the index indicated by heap_index.
        :param heap_index: the index of the heap to update
        :type heap_index: int
        :param amount: the amount to remove from the heap
        :type amount: int
        :return: None
        """
        heap = self.__heaps[heap_index]
        heap.remove(amount)

    def is_heap_empty(self, heap_index):
        """
        Checks if the heap has a value of 0 and returns a True if it is empty
        and a False otherwise.
        :param heap_index: Index of the heap
        :type heap_index: int
        :return: Returns true if the heap is empty, and false otherwise
        :rtype: boolean
        """
        heap = self.get_heap(heap_index)
        return heap.current_size == 0

    def is_amount_valid(self, heap_index, amount):
        """
        Checks if the amount to remove from the heap is less than or
        equal to the current heap size. Amount cannot be zero, if it is,
        return a False.
        :param heap_index: Index of the heap
        :type heap_index: int
        :param amount: The amount to remove from the heap
        :type amount: int
        :return: Returns True if the amount to remove from the heap
        is less than or equal to the heap amount, and False otherwise.
        Returns False if amount is zero.
        :rtype: boolean
        """

        if amount <= 0:
            return False
        heap = self.get_heap(heap_index)
        return amount <= heap.current_size

    def print_heaps(self):
        """
        Prints the following:
        Heap <heap number> size: <current heap size>
        :return: None
        """
        for i, heap in enumerate(self.__heaps):
            print(f"Heap {i + 1} size: {heap.current_size}")

    def is_game_over(self):
        """
        Boolean function returns if the game is over. Goes through all of the
        heaps to see if all of the heap
        sizes are 0.
        :return: True if all heap sizes are 0, and False otherwise
        :rtype: boolean
        """
        for heap in self.__heaps:
            if heap.current_size > 0:
                return False
        return True

    def reset(self):
        """
        Resets the heap sizes to the initial_size, and sets turn_index to 0.
        :return: None
        """
        for heap in self.__heaps:
            heap.reset()
        self.__turn_index = 0

    def increment_player_score(self, player_index):
        """
        increments the player's score in the player list indicated by
        player_index by 1.
        :param player_index:
        :type
        :return: None
        """
        # get the player object from the player list
        player = self.__players[player_index]
        # increment the player's score by 1
        player.score += 1

    def print_player_scores(self):
        """
        Prints the player scores in the following format:
        Player <player index + 1> score: <score>
        :return: None
        """
        for i, player in enumerate(self.__players):
            print(f"Player {i + 1} score: {player.score}")

    def print_round_winner(self):
        """
        Prints the player winner for the round in the following format:
        Player <player name> has won this round!
        :return: None
        """
        winner_index = 0
        max_score = self.__players[0].score
        for i, player in enumerate(self.__players):
            if player.score > max_score:
                winner_index = i
                max_score = player.score
        print(f"Player {self.__players[winner_index].name} has won this round!")
