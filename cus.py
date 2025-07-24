# Customer Management System

# Input: number of customers to enter
num_customers = int(input("Enter number of customers: "))

# Open file for writing customer data
with open("customers.txt", "w") as file:
    file.write("CustomerID\tName\t\tPhone\t\tEmail\n")
    file.write("-" * 60 + "\n")

    # Loop to get data for each customer
    for i in range(num_customers):
        print(f"\nEnter details for customer {i + 1}:")
        customer_id = input("Customer ID: ")
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email Address: ")

        # Write to file
        file.write(f"{customer_id}\t{name}\t{phone}\t{email}\n")

        # Optional: Print confirmation
        print(f"Customer {name} (ID: {customer_id}) saved.")

print("\nAll customer data has been written to 'customers.txt'")
