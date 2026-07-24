EXCHANGE_RATE = 35.5

print("Choose conversion direction:")
print("1. THB to USD")
print("2. USD to THB")
choice = input("Enter choice (1 or 2): ")

amount = float(input("Enter amount to convert: "))

if choice == "1":
    result = amount / EXCHANGE_RATE
    print(f"Formula: {amount} THB / {EXCHANGE_RATE} = {result:.2f} USD")
    print(f"Converted Amount: {result:.2f} USD")
elif choice == "2":
    result = amount * EXCHANGE_RATE
    print(f"Formula: {amount} USD * {EXCHANGE_RATE} = {result:.2f} THB")
    print(f"Converted Amount: {result:.2f} THB")
else:
    print("Invalid choice! Please select 1 or 2.")