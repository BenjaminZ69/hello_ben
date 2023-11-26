Numbers = [4, 9, 1, 0, 34, 67, 2]

Numbers.append(42)
print(Numbers)

Numbers2 = Numbers.copy()
print(Numbers2)

print(Numbers.count(0))

Numbers.insert(2, 23)
print(Numbers)

Numbers.reverse()
print(Numbers)

Numbers.remove(67)
print(Numbers)

Numbers.sort()
print(Numbers)

Numbers.pop()
print(Numbers)

Numbers.extend(Numbers2)
print(Numbers)

print(Numbers.index(34))