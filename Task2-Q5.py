string=input("enter input ")
rev_string=""
for char in string:
    rev_string=char+rev_string
if string==rev_string:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")
