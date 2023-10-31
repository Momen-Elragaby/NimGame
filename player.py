class Player:

    """
    Class representing a player in the game.
    author(s): Momen Elragaby
    :param player_name: The name of the player.
    :type player_name: str
    """

    def __init__(self, player_name):

        """
        Constructor that initializes a player with a name and a score of 0.
        :param player_name: The name of the player.
        :type player_name: str
        :param 0: The score of the player.
        :type 0: int
        """

        self.__name = player_name
        self.__score = 0

    @property
    def name(self):

        """
        Getter method that returns the name of the player.
        :return: The name of the player.
        :rtype: str
        """

        return self.__name

    @property
    def score(self):

        """
        Getter method that returns the score of the player.
        :return: The score of the player.
        :rtype: int
        """

        return self.__score

    @score.setter
    def score(self, amount):
        """
        Increments the player's score by 1.
        :return: None
        """

        self.__score += amount

    def increment_score(self):
        """
        increment_score updates the player's `Player.score` by one point<br>
        :return: updated score<br>
        :return: None
        """
        #pass

        self.__score += 1


