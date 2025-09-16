places = ["tokyo", "los angeles", "dubai", "france", "brazil"]

print("Original list:", places)
print("Sorted list:", places)
print("Original still:", places)

print("Reverse-sorted list:", sorted(places, reverse=True))
print("Original still:", places)

places.reverse()
print("Reversed list:", places)

places.sort()
print("Back to original ordewr", places)

places.sort()
print("Sorted permanently:", places)

places.sort(reverse=True)
print("Sorted permanently in reverese:", places)