visited_cities = ["Seville", "Malaga", "Zagreb", "Malaga"]

unique_cities = set(visited_cities)
print (f"Visited cities: {unique_cities}")

zagreb_expenses = {
    "food": 10,
    "transport": 20,
    "souvenirs": 20
}

user_request = input("Enter expense category: ")
clean_user_request = user_request.strip().lower()

expense_ammount = zagreb_expenses.get(clean_user_request, "No data")
print (f"Amount for {clean_user_request}: {expense_ammount}")