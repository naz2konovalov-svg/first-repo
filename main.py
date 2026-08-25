items_for_sale = ["Polo Ralph Lauren", "Burberry", "New Rock", "Burberry", "Nike"]
print(f"Items for sale: {items_for_sale}")

unique_brands = set(items_for_sale)
print(f"Brands: {unique_brands}")

jacket_details = {
    "brand": "Polo Ralph Lauren",
    "size": "M",
    "price": 500
}

price = jacket_details.get("price")
print(f"Price: {price}")

clients_message = "How much?"

clean_clients_message = clients_message.strip().lower()
print(f"Clients message: {clean_clients_message}")