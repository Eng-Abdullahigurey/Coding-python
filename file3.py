# File name
file_name = "input.txt"

# Lists to store data
customer_name = []
order_id = []
mobile = []

print("Reading from file:", file_name)

# Read the file
try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        if not lines:
            print("File is empty.")
        for line in lines:
            if line.strip():  # Skip empty lines
                # Split and strip parts
                parts = [p.strip() for p in line.strip().split(",")]
                if len(parts) == 3:
                    customer_name.append(parts[0])
                    order_id.append(parts[1])
                    mobile.append(parts[2])
                else:
                    print("Invalid line format:", line.strip())
except FileNotFoundError:
    print("File not found. Created a new one.")
    open(file_name, "w").close()

# Display the data
if customer_name:
    print("\nCustomer Data:")
    for i in range(len(customer_name)):
        print(f"{i+1}. Name: {customer_name[i]}, Order ID: {order_id[i]}, Mobile: {mobile[i]}")
else:
    print("\nNo valid customer data found.")
