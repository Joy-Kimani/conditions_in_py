def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

#prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#calculating the final price
final_price = calculate_discount(original_price, discount_percent)

#printing the result
if final_price < original_price:
    print(f"The final price after applying the discount is: ksh{final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ksh{original_price:.2f}")
