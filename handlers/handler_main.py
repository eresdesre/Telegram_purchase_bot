# Importing the HandlerCommands class for command processing
from handlers.handler_com import HandlerCommands
# Importing the HandlerAllText class for processing button presses and other messages
from handlers.handler_all_text import HandlerAllText
# Importing the HandlerInlineQuery class for handling inline button presses.
from handlers.handler_inline_query import HandlerInlineQuery


class HandlerMain:
    """
    Composite class
    """
    def __init__(self, bot):
        # Getting our bot
        self.bot = bot
        # Here will be the initialization of handlers
        self.handler_commands = HandlerCommands(self.bot)
        self.handler_all_text = HandlerAllText(self.bot)
        self.handler_inline_query = HandlerInlineQuery(self.bot)

    def handle(self):
        # Here will be the launch of handlers
        self.handler_commands.handle()
        self.handler_all_text.handle()
        self.handler_inline_query.handle()
