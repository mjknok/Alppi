lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Roope", "Teemu", "Petro", "Petro", "Kukkis", "Pepo"]
friends[1] = "Mika"
friends.extend(lucky_numbers)
friends.append("Esko")

friends.insert(1, "Ossi")

friends.remove("Petro")

friends.pop()
friends.sort
print(friends.index("Kukkis"))
print(friends.count ("Petro"))
lucky_numbers.sort()

friends2 = friends.copy()
print(friends)
print(lucky_numbers)
print(friends2)


