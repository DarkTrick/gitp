class CommandException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__cause__ = None
        self.__suppress_context__ = True
