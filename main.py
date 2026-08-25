inventory = ["кирка", "земля", "алмаз", "земля", "дерево"]
inventory.append("меч")
print(f"Весь инвентарь: {inventory}")

unique_items = set(inventory)
print(f"Уникальные ресурсы: {unique_items}")

hotbar = inventory[0:3]
print(f"Быстрый доступ: {hotbar}")

player_stats = {
    "name": "Nazar",
    "level": 16,
    "health": 100
}

weapon = player_stats.get("weapon", "Оружие не найдено")
print(f"Статус оружия: {weapon}")

chat_message = "   ВНИМАНИЕ! КРИПЕР СЗАДИ!   "

clean_message = chat_message.strip().lower()
print(f"Чат гильдии: {clean_message}")