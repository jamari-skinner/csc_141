sandwich_orders = ['turkey', 'pastrami', 'ham', 'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())