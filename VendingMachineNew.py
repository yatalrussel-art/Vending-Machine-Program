import sys

# Simulation of the Vending Machine with Stock
items = [
    {'code': 0, 'name': 'Coca Cola', 'price': 1.50, 'stock': 5},
    {'code': 1, 'name': 'Orange Juice', 'price': 2.25, 'stock': 3},
    {'code': 2, 'name': 'Pepsi', 'price': 1.00, 'stock': 6},
    {'code': 3, 'name': 'Hot Coco', 'price': 1.75, 'stock': 4},
    {'code': 4, 'name': 'Kitkat', 'price': 0.75, 'stock': 5},
    {'code': 5, 'name': 'Dorito Chips', 'price': 1.20, 'stock': 2},
    {'code': 6, 'name': 'Snickers', 'price': 0.85, 'stock': 3},
]

# Function to display Available Items
def display_items():
    print("\n--- Vending Machine Menu ---")
    print("Code | Item Name      | Price | Stock")
    print("-----|----------------|-------|------")
    for item in items:
        print(f" {item['code']:<3} | {item['name']:<14} | ${item['price']:.2f} | {item['stock']}")
    print("-------------------------------------")

# Function to get item by code
def get_item_by_code(code):
    for item in items:
        if item['code'] == code:
            return item
    return None

# Main Program
def vending_machine():
    current_balance = 0.0

    print("Welcome to the Vending Machine!")

    # Main Loop
    while True:
        display_items()
        print(f"Current Balance: **${current_balance:.2f}**")

        user_input = input(
            "\nInsert money first before purchase or type EXIT: "
        ).strip().upper()

        # Exit condition
        if user_input == 'EXIT':
            if current_balance > 0:
                print(f"\nReturning remaining change: **${current_balance:.2f}**")
            print("Thank you for using the vending machine!")
            break

        # Try item code first
        try:
            code = int(user_input)
            selected_item = get_item_by_code(code)

            if selected_item is None:
                print("Invalid code. Please select a code from the list.")
                continue

            # Stock check
            if selected_item['stock'] <= 0:
                print(f"Sorry, {selected_item['name']} is out of stock!")
                continue

        except ValueError:
            # Try money input
            try:
                amount = float(user_input)
                if amount > 0:
                    current_balance += amount
                    print(f"**${amount:.2f}** inserted. New Balance: **${current_balance:.2f}**")
                    continue
                else:
                    print("Please insert a positive amount.")
                    continue
            except ValueError:
                print("Invalid input. Enter money, an item code, or EXIT.")
                continue

        # Purchase processing
        item_price = selected_item['price']
        if current_balance < item_price:
            needed = item_price - current_balance
            print(f"Insufficient funds. You need **${needed:.2f}** more.")
            continue

        # Deduct balance and stock
        current_balance -= item_price
        selected_item['stock'] -= 1

        print(f"\n**Dispensing:** {selected_item['name']}")
        print(f"**Remaining Balance:** **${current_balance:.2f}**")

        if selected_item['stock'] == 0:
            print(f"{selected_item['name']} is now out of stock!")

        # Purchase Continuation
        cont = input("\nDo you want to make another purchase? (y/n): ").strip().lower()
        yes_responses = ['y', 'yes', 'yup', 'sure', 'yeah', 'ok', 'okay']

        if cont in yes_responses:
            continue
        else:
            if current_balance > 0:
                print(f"\nReturning remaining change: **${current_balance:.2f}**")
            print("Thank you for using the vending machine!")
            break

if __name__ == "__main__":
    vending_machine()
