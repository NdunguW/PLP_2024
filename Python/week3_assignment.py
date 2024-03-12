"""
PLP week three assignment:
Objective: Functions in Python
"""


# create a function
def calculate_discount(price, discount_percent):
    """
        Calculates the final price after applying a discount.

        Args:
            price (float): The original price.
            discount_percent (float): The discount percentage (e.g., 20 for 20%).

        Returns:
            float: The final price after applying the discount (or the original price if discount is less than 20%).
        """

    if discount_percent >= 20:
        # calculate discount amount
        discount_amount = (discount_percent / 100) * price
        print("Discount= Ksh", discount_amount)

        # calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# example: get user input
original_price = float(input("Enter the original price: "))
discount_percentage = int(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)
# display final price with 2 decimal places
print(f"The selling price after discount= Ksh {final_price:.2f}")
