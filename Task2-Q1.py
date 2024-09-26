my_string = "Guvi Geeks Network Private Limited"
count_characters = "aeiou"
characters_frequency = {}

for char in my_string:
    if char in count_characters:
        if char in characters_frequency:
            characters_frequency[char] += 1
        else:
            characters_frequency[char] = 1

print(characters_frequency)
print(sum(characters_frequency.values()))

            

