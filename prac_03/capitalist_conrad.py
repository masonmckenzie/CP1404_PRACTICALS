"""
CP1404/CP5632 - Practical - Mason McKenzie
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
"""
import random
# setting the constants
starting_price = 10  # starting price is 10$
maximum_increase = 0.10  # max increase is equal to 10%
maximum_decrease = 0.05  # max decrease is equal to 5%
maximum_price = 1000  # $
minimum_price = 0.001  # $
output_file = "stock_value.txt"

out_file = open(output_file, "w")  # opens the 'output_file where 'w' is used for writting in file
day = 0
value = starting_price
print("starting price: ${:,.2f}".format(value), file=out_file)

while minimum_price <= value <= maximum_price:
    value_change = 0
    day += 1
    if random.randint(1, 2) == 1:
        value_change = random.uniform(0, maximum_increase)
    else:
        value_change = random.uniform(-maximum_decrease, 0)

    value *= (1 + value_change)
    print("${:,.2f}) the value for day".format(day, value), file=out_file)


out_file.close()