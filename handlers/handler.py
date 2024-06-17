# Importing the abc library for implementing abstract classes
import abc
# Importing keyboard layout and keys
from markup.markup import Keyboards
# Importing a manager class to work with the library
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # Obtaining the bot object
        self.bot = bot
        # Initializing button markup
        self.keybords = Keyboards()
        # Initializing the manager for working with the database
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
