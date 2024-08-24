names = ["Alice", "Bob", "Charlie"]
print(names[0])
print(names[1])
print(names[2])




names = ["Alice", "Bob", "Charlie"]
print(f"Hello, {names[0]}!")
print(f"Hello, {names[1]}!")
print(f"Hello, {names[2]}!")



transport = ["Honda motorcycle", "Tesla car", "Boeing airplane"]
print(f"I would like to own a {transport[0]}.")
print(f"I would like to own a {transport[1]}.")
print(f"I would like to own a {transport[2]}.")



guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")




guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print(f"Sorry, {guests[1]} can't make it.")

# Replace the guest who can't make it
guests[1] = "Charles Darwin"

# New invitation messages
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are still invited to dinner.")





guests = ["Albert Einstein", "Charles Darwin", "Isaac Newton"]
print("I found a bigger table!")

# Add more guests
guests.insert(0, "Nikola Tesla")
guests.insert(2, "Galileo Galilei")
guests.append("Ada Lovelace")

# New invitation messages
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")







while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Let the remaining guests know they're still invited
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner.")

# Remove the last two guests and print the empty list
del guests[0]
del guests[0]

print(guests)  # Output: []





places = ["Japan", "Norway", "Brazil", "Australia", "Canada"]

# Original order
print(places)

# Alphabetical order without modifying the list
print(sorted(places))

# Confirm original order
print(places)

# Reverse alphabetical order without modifying the list
print(sorted(places, reverse=True))

# Confirm original order
print(places)

# Reverse the list
places.reverse()
print(places)

# Reverse the list again to return to original order
places.reverse()
print(places)

# Sort the list alphabetically
places.sort()
print(places)

# Sort the list in reverse alphabetical order
places.sort(reverse=True)
print(places)








languages = ["Python", "Java", "C++", "Ruby", "JavaScript"]

# Using append()
languages.append("Swift")
print(languages)

# Using insert()
languages.insert(2, "Go")
print(languages)

# Using remove()
languages.remove("Java")
print(languages)

# Using pop()
popped_language = languages.pop()
print(popped_language)
print(languages)

# Using sort()
languages.sort()
print(languages)

# Using reverse()
languages.reverse()
print(languages)

# Using count()
print(languages.count("Python"))

# Using index()
print(languages.index("C++"))

# Using clear()
languages.clear()
print(languages)





languages = ["Python", "Java", "C++", "Ruby", "JavaScript"]
# Intentional Index Error
print(languages[10])  # This will raise an IndexError since there's no item at index 10












