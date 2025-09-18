favorite_pizzas = ["pepperoni", "margherita", "hawaiian", "bbq chicken", "veggie"]

print("My first three favorite pizzas are:")
for pizza in favorite_pizzas[:3]:  
    print(pizza.title())

middle_index_start = 1
middle_index_end = 4
print("\nSome of my middle favorite pizzas are:")
for pizza in favorite_pizzas[middle_index_start:middle_index_end]:
    print(pizza.title())

print("\nMy last three favorite pizzas are:")
for pizza in favorite_pizzas[-3:]: 
    print(pizza.title())

print("\nI really love these pizzas!")
