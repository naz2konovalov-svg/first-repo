prices = [120, 45, 300, 15, 80]
for index, item in enumerate(prices):
    if item <= 50:
        continue
    if item >= 100:
        new_price = item - 20
        print(f"Discount price: {new_price}")
    else:
        print(f"Normal price: {item}")


while True:
    user_input = input("Enter your age: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Numbers only!")
        continue
    if user_input >= 120:
        print("Write your real age please!")
        continue 
    if user_input < 18:
        print("Too young!")
        break
    else:
        print("Success! Welcome!")
        break