#Creating a function named calculate_discount.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = (price * discount_percent) / 100
        final_price = price - discount
        return final_price
    else:
        return price


# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price is: {final_price}")
