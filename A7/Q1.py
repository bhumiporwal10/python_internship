import re


email = "bhumi123@gmail.com"
email_pattern = r'\w+@\w+\.\w+'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


mobile = "9876543210"
mobile_pattern = r'^[6-9]\d{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

text = "I love listening to BTS songs!"
word = "BTS"

if re.search(word, text):
    print("Word 'BTS' is present")
else:
    print("Word 'BTS' is not present")
