def calculate_price(base_price, tax_rate, discount=0):
    """
    Calculates the final price of an item.
    """
    if base_price < 0:
        raise ValueError("Price cannot be negative")

    tax = base_price * tax_rate
    final_price = base_price + tax

    if discount > 0:
        final_price = final_price * (1 - discount)

    return final_price
