string=input("Enter input ")
vowels_string="aeiou"
print("Input string ",string)
for char in string:
    if char in vowels_string:
        string=string.replace(char,"")
print("output string without vowels ",string)

