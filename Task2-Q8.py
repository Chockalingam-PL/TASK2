string1=input("enter string1 ")
string2=input("enter string2 ")

if len(string1)!=len(string2):
    print("Not anagrams")
else:
    if sorted(string1)==sorted(string2):
        print("Answers are anagram")
    else:
        print("not anagrams")
