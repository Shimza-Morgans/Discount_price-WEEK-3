def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after applying the discount, or the original price if discount is less than 20%
    """
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))
    
    # Calculate and print the final price
    final_price = calculate_discount(original_price, discount)
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
