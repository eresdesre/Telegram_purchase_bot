# Importing the response to the user
from settings.message import MESSAGES
from settings import config, utility
# Importing the parent class
from handlers.handler import Handler


class HandlerAllText(Handler):
    """
    The class processes incoming text messages from button presses
    """

    def __init__(self, bot):
        super().__init__(bot)
        # Step in the order
        self.step = 0

    def pressed_btn_category(self, message):
        """
        Handling the event of pressing the 'Select Product' button. More precisely,
	this is selecting the category of products
        """
        self.bot.send_message(message.chat.id, "Catalog of product categories",
                              reply_markup=self.keybords.remove_menu())
        self.bot.send_message(message.chat.id, "Make your choice",
                              reply_markup=self.keybords.category_menu())

    def pressed_btn_info(self, message):
        """
        Handling the event of pressing the 'About the Store' button'
        """
        self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.info_menu())

    def pressed_btn_settings(self, message):
        """
        Handling the event of pressing the 'Settings' button'
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keybords.settings_menu())

    def pressed_btn_back(self, message):
        """
        Handling the event of pressing the 'Back' button'
        """
        self.bot.send_message(message.chat.id, "You have returned back",
                              reply_markup=self.keybords.start_menu())

    def pressed_btn_product(self, message, product):
        """
        Handling the event of pressing the 'Select Product' button, specifically
	 selecting a product from the category
        """
        self.bot.send_message(message.chat.id, 'Category ' +
                              config.KEYBOARD[product],
                              reply_markup=self.keybords.set_select_category(
                                  config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, "Ок",
                              reply_markup=self.keybords.category_menu())

    def pressed_btn_order(self, message):
        """
        Processes incoming text messages from pressing the 'Order' button.
        """
        # Resetting step data
        self.step = 0
        # Getting a list of all items in the order
        count = self.BD.select_all_product_id()
        # Obtaining the quantity of each item in the order position
        quantity = self.BD.select_order_quantity(count[self.step])

        # Sending the response to the user
        self.send_message_order(count[self.step], quantity, message)

    def send_message_order(self, product_id, quantity, message):
        """
        Sends a response to the user when performing various actions
        """
        self.bot.send_message(message.chat.id,MESSAGES['order_number'].format(
            self.step+1), parse_mode="HTML")
        self.bot.send_message(message.chat.id,
                              MESSAGES['order'].
                              format(self.BD.select_single_product_name(
                                  product_id),
                                     self.BD.select_single_product_title(
                                         product_id),
                                     self.BD.select_single_product_price(
                                         product_id),
                                     self.BD.select_order_quantity(
                                         product_id)),
                              parse_mode="HTML",
                              reply_markup=self.keybords.orders_menu(
                                  self.step, quantity))

    def pressed_btn_up(self, message):
        """
        Handling the press of the increase quantity button
	for a specific item in the order
        """
        # Getting a list of all products in the order
        count = self.BD.select_all_product_id()
        # Getting the quantity of a specific item in the order
        quantity_order = self.BD.select_order_quantity(count[self.step])
        # Getting the quantity of a specific item in the products
        quantity_product = self.BD.select_single_product_quantity(
            count[self.step])
        # If the item exists
        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1
            # Making changes to the orders database
            self.BD.update_order_value(count[self.step],
                                       'quantity', quantity_order)
            # Making changes to the product database
            self.BD.update_product_value(count[self.step],
                                         'quantity', quantity_product)
        # Sending the response to the user
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_douwn(self, message):
        """
        Handling the press of the decrease quantity button
	for a specific item in the order
        """
        # Getting a list of all items in the order
        count = self.BD.select_all_product_id()
        # Getting the quantity of a specific item in the order
        quantity_order = self.BD.select_order_quantity(count[self.step])
        # Getting the quantity of a specific item in the products
        quantity_product = self.BD.select_single_product_quantity(
            count[self.step])
        # If the item is in the order
        if quantity_order > 0:
            quantity_order -= 1
            quantity_product += 1
            # Making changes to the 'orders' database
            self.BD.update_order_value(count[self.step],
                                       'quantity', quantity_order)
            # Making changes to the 'product' database

            self.BD.update_product_value(count[self.step],
                                         'quantity', quantity_product)
        # Sending the response to the user
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_x(self, message):
        """
         Handling the press of the delete button
	 for an item in the order position
        """
        # Getting a list of all product_ids in the order
        count = self.BD.select_all_product_id()
        # If the list is not empty
        if count.__len__() > 0:
            # Getting the quantity of a specific item in the order
            quantity_order = self.BD.select_order_quantity(count[self.step])
            # Getting the quantity of a specific product
            # Order position to return to product
            quantity_product = self.BD.select_single_product_quantity(
                count[self.step])
            quantity_product += quantity_order
            # Making changes to the 'orders' database
            self.BD.delete_order(count[self.step])
            # Making changes to the 'product' database
            self.BD.update_product_value(count[self.step],
                                         'quantity', quantity_product)
            # Decreasing the step
            self.step -= 1

        count = self.BD.select_all_product_id()
       # If the list is not empty
        if count.__len__() > 0:

            quantity_order = self.BD.select_order_quantity(count[self.step])
            # Sending a message to the user
            self.send_message_order(count[self.step], quantity_order, message)

        else:
            # If the item is not in the order, send a message
            self.bot.send_message(message.chat.id, MESSAGES['no_orders'],
                                  parse_mode="HTML",
                                  reply_markup=self.keybords.category_menu())

    def pressed_btn_back_step(self, message):
        """
        Handling the press of the button to move to earlier items in the order
        """
        # Decreasing the step until the step is equal to "0"
        if self.step > 0:
            self.step -= 1
        # Getting a list of all items in the order
        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])

        # Sending the response to the user
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_next_step(self, message):
        """
        Handling the press of the button to move to later items in the order
        """
        # Increasing the step until the step equals the number of rows
        # Order fields with price calculation starting from "0"
        if self.step < self.BD.count_rows_order() - 1:
            self.step += 1
        # Getting a list of all products in the order
        count = self.BD.select_all_product_id()
        # Getting the quantity of a specific item according to the sampling step
        quantity = self.BD.select_order_quantity(count[self.step])

        # Sending the response to the user
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_apllay(self, message):
        """
        Handles incoming text messages from pressing the 'Place Order' button
        """
        # Sending the response to the user
        self.bot.send_message(message.chat.id,
                              MESSAGES['applay'].format(
                                  utility.get_total_coas(self.BD),

                                  utility.get_total_quantity(self.BD)),
                              parse_mode="HTML",
                              reply_markup=self.keybords.category_menu())
        # Clearing the data from the order
        self.BD.delete_all_order()

    def handle(self):
        # Message handler
        # Which handles incoming text messages from button presses.
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):
            # ********** Menu ********** #

            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['ORDER']:
                # если есть заказ
                if self.BD.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(message.chat.id,
                                          MESSAGES['no_orders'],
                                          parse_mode="HTML",
                                          reply_markup=self.keybords.
                                          category_menu())

            # ********** Menu (product categories, dairy products, groceries, ice cream)******
            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')

            # ********** Order menu **********

            if message.text == config.KEYBOARD['UP']:
                self.pressed_btn_up(message)

            if message.text == config.KEYBOARD['DOWN']:
                self.pressed_btn_douwn(message)

            if message.text == config.KEYBOARD['X']:
                self.pressed_btn_x(message)

            if message.text == config.KEYBOARD['BACK_STEP']:
                self.pressed_btn_back_step(message)

            if message.text == config.KEYBOARD['NEXT_STEP']:
                self.pressed_btn_next_step(message)

            if message.text == config.KEYBOARD['APPLAY']:
                self.pressed_btn_apllay(message)
            # Other button presses and user input
            else:
                self.bot.send_message(message.chat.id, message.text)
