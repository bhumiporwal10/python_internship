import csv

data = [
    ["Name", "Address", "Mobile", "Email"],
    ["Amit", "Delhi", "9876543210", "amit@example.com"],
    ["Sneha", "Mumbai", "9123456789", "sneha@example.com"],
    ["Ravi", "Bangalore", "9988776655", "ravi@example.com"]
]

with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully!")
