# Converts a list like p[(5,),(8,),...] к [5,8,...]
def _convert(list_convert):

    return [itm[0] for itm in list_convert]


# To calculate the total sum of the order and return the result
def total_coast(list_quantity, list_price):

    order_total_cost = 0

    for ind, itm in enumerate(list_price):
        order_total_cost += list_quantity[ind]*list_price[ind]

        return order_total_cost


# To calculate the total quantity of ordered units of goods and return the result
def total_quantity(list_quantity):

    order_total_quantity = 0

    for itm in list_quantity:
        order_total_quantity += itm

        return order_total_quantity


def get_total_coas(BD):
    """
    Returns the total cost of the goods
    """
    # Retrieve the list of all product IDs in the order
    all_product_id = BD.select_all_product_id()
    # Retrieve the list of costs for all items in the order as a regular list
    all_price = [BD.select_single_product_price(itm) for itm in all_product_id]
    # Retrieve the list of quantities for all items in the order as a regular list.
    all_quantity = [BD.select_order_quantity(itm) for itm in all_product_id]
    # Returns the total cost of the goods
    return total_coast(all_quantity,all_price)


def get_total_quantity(BD):
    """
    Returns the total quantity of ordered units of goods
    """
    # Retrieve the list of all product IDs in the order
    all_product_id = BD.select_all_product_id()
    # Retrieve the list of quantities for all items in the order as a regular list
    all_quantity = [BD.select_order_quantity(itm) for itm in all_product_id]
    # Returns the number of product items
    return total_quantity(all_quantity)
