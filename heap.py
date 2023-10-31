class Heap:
    """
    This class represents a heap of objects in the game of NIM.
    author(s): Momen Elragaby
    :param size: the initial size of the heap
    :type size: int
    """
    def __init__(self, size):
        """
        Initializes a heap object with the given initial size.
        :param size: the initial size of the heap
        :type size: int
        """
        self.__initial_size = size
        self.__current_size = self.__initial_size

    @property
    def initial_size(self):
        """
        Returns the initial size of the heap.
        :return: the initial size of the heap
        :rtype: int
        """
        return self.__initial_size

    @property
    def current_size(self):
        """
        Returns the current size of the heap.
        :return: the current size of the heap
        :rtype: int
        """
        return self.__current_size

    @initial_size.setter
    def initial_size(self, initial_size):
        """
        Sets the initial size of the heap.
        :param initial_size: the new initial size of the heap
        :type initial_size: int
        :return: None
        """
        self.__initial_size = initial_size

    @current_size.setter
    def current_size(self, current_size):
        """
        Sets the current size of the heap.
        :param current_size: the new current size of the heap
        :type current_size: int
        :return: None
        """
        self.__current_size = current_size

    def remove(self, amount):
        """
        Removes the specified amount of objects from the heap.
        Returns -1 if the current size of the heap minus the amount is less
        than 0. Otherwise, it returns the new size of the heap.
        :param amount: the number of objects to remove from the heap
        :type amount: int
        :return: the new size of the heap or -1 if the amount was invalid
        :rtype: int
        """
        if self.__current_size - amount < 0:
            return -1

        self.__current_size -= amount
        return self.__current_size

    def reset(self):
        """
        Resets the current size of the heap to the initial size.
        :return: None
        """
        self.__current_size = self.__initial_size
