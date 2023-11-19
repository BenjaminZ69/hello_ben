monthConversions = {
    "Ben" : "Benji",
    "Stan" : "Stanley",
    "Q" : "Qunta",
}

print(monthConversions)
print(monthConversions["Stan"])
print(monthConversions.get("Q"))
print(monthConversions.get("Rog"))
print(monthConversions.get("Rog", "Not take class today"))