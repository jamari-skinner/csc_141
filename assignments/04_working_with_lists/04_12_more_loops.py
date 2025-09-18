sandwich_orders = ["turkey", "ham", "veggie", "pb&j"]
finished_sandwiches = []

for order in sandwich_orders:
    print("I made your " + order + " sandwich.")
    finished_sandwiches.append(order)

print("\nAll sandwiches are finished:")
for sandwich in finished_sandwiches:
    print(sandwich.title() + " Sandwich")
