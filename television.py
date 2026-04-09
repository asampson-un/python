
class Television:
    MIN_VOLUME :int = 0
    MAX_VOLUME :int = 2
    MIN_CHANNEL :int = 0
    MAX_CHANNEL :int = 3

    def __init__(self) -> None:
        """
        Initialize instance variables
        """
        self.__status :bool = False
        self.__muted :bool = False
        self.__volume :int = Television.MIN_VOLUME
        self.__channel :int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to power on/off tv
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute or unmute tv
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status: #tv on?
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else: #not max channel
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status: #tv on?
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else: #not min channel
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the tv volume
        """
        if self.__status: #tv on?
            self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume
        """
        if self.__status: #tv on?
            self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status, channel and volume
        :return: tv status, tv channel and tv volume
        """
        if self.__muted:
            _vol = Television.MIN_VOLUME
        else:
            _vol = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {_vol}"