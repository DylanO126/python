class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        '''
        Method to set default values for Television Class
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        """
        Method to switch boolean value of status trait
        """
        self.__status = bool((self.__status + 1) % 2)

    def mute(self) -> None:
        """
        Method to switch boolean value of muted trait
        """
        if self.__status:
            self.__muted = bool((self.__muted + 1) % 2)

    def channel_up(self) -> None:
        """
        Method to increase the channel trait by 1
        if at max then restart at zero
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Method to decrease the channel trait by 1
        if at min the jump to max
        """
        if self.__status:
            self.__channel = (self.__channel - 2) % (Television.MAX_CHANNEL + 1)
            self.__channel += 1

    def volume_up(self) -> None:
        """
        Method to increase the volume trait by 1
        if at max do nothing
        if muted = True switch to False
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume trait by 1
        if at min do nothing
        if muted = True switch to False
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Operation Overload for string type for the television class
        if TV is muted Volume should be Min value
        :return: formated string according to instructions
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
