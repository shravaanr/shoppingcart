total = 0
foods = []
prices = []

while True:
    food = input("Enter the food name (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = input('Enter the price: ')
        foods.append(food)
        prices.append(float(price))  # Convert price to float
    
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"Total: {total}")