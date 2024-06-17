# Importing the parent class
from handlers.handler import Handler
# Importing user messages
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
    """
    The class processes incoming text messages from pressing inline buttons
    """

    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_product(self, call, code):
        """
        The class handles incoming requests for pressing inline product buttons
        """
        # Creating a record in the database upon ordering
        self.BD._add_orders(1, code, 1)

        self.bot.answer_callback_query(
            call.id,
            MESSAGES['product_order'].format(
                self.BD.select_single_product_name(code),
                self.BD.select_single_product_title(code),
                self.BD.select_single_product_price(code),
                self.BD.select_single_product_quantity(code)),
            show_alert=True)

    def handle(self):
        # Handler (decorator) for requests from pressing product buttons.
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            code = call.data
            if code.isdigit():
                code = int(code)

            self.pressed_btn_product(call, code)
