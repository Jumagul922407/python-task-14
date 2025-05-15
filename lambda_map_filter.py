# lambda_map_filter.py

# Сан тизмеси
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Бардык сандарды 2ге көбөйтүү (map)
doubled = list(map(lambda x: x * 2, numbers))
print("2ге көбөйтүлгөн сандар:", doubled)

# Жуп сандарды алуу (filter)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Жуп сандар:", even_numbers)
