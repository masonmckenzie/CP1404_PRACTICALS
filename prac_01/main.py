products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = [product for product in products if product[2]]
print(on_sale_products)