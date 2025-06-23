num = input("Enter a number: ")
reverse = num[::-1]
if num == reverse:
    print(num, "is a Palindrome Number.")
else:
    print(num, "is not a Palindrome Number.")
