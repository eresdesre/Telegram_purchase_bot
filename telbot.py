from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    """
        The main class of a Telegram bot (server), based on the pyTelegramBotAPI library
    """

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):

        self.token = config.TOKEN
        self.bot = TeleBot(self.token)
        self.handler = HandlerMain(self.bot)


    def start(self):
        """
            The method is intended to start the event handler
        :param self:
        :return:
        """

        self.handler.handle()

    def run_bot(self):

        """
            The method launches the main server events
        :param self:
        :return:
        """

        self.start()
        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    bot = TelBot()
    bot.run_bot()
