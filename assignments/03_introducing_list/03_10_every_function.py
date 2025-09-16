games = ["baseball", "football", "basketball", "soccer"]

print("Original list:", games)

games.append("hockey")
print("After append:", games)

games.insert(2, "tennis")
print("After insert:", games)

del games[0]
print("After del:", games)

popped_game = games.pop()
print("Popped:", popped_game)
print("After pop:", games)

games.remove("tennis")
print("After remove:", games)

games.sort()
print("Sorted:", games)

games.sort(reverse=True)
print("Reverse sorted:", games)

print("Temporarily sorted:", sorted(games))
print("Original after sorted():", games)

games.reverse()
print("After reverse:", games)

print("Length of list:", len(games))