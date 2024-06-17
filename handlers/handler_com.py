# Importing the parent class
from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    The class handles incoming commands like /start and /help, etc.
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        # Handles incoming /start commands
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' Hello! Im ready for further tasks.',
                              reply_markup=self.keybords.start_menu())

    def handle(self):
        # Message handler,
        # Handler (decorator) that handles incoming /start commands.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(type(message))
            if message.text == '/start':
                self.pressed_btn_start(message)
