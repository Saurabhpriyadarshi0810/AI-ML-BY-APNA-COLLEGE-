word = input ("enter word to check palindrome :").strip().lower()

x = word[::-1]
 

if word == x :
    print( f" {word} is palindrome ")
else:
    print(f"{word} is not palindrome")