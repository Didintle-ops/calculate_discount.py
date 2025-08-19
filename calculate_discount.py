def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is 20% or higher"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Get user input
original_price = float(input("Enter the original price: $"))
discount = float(input("Enter the discount percentage: "))

# Calculate and display result
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")