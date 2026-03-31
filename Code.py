import time

def add_transaction(transactions, type, amount, description):
    """Adds a new income or expense transaction."""
    # Ensure amount is a positive number
    try:
        amount = float(amount)
        if amount <= 0:
            print("\n❌ Amount must be greater than zero.")
            return
    except ValueError:
        print("\n❌ Invalid amount. Please enter a number.")
        return

    # Assign a unique ID and current timestamp
    transaction_id = int(time.time() * 1000) # Simple unique ID using milliseconds
    
    # Store the transaction
    transactions[transaction_id] = {
        'type': type,  # 'Income' or 'Expense'
        'amount': amount,
        'description': description,
        'date': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    print(f"\n✅ Successfully added {type}: ${amount:.2f} ({description})")

def calculate_balance(transactions):
    """Calculates the current balance (Total Income - Total Expense)."""
    total_income = sum(t['amount'] for t in transactions.values() if t['type'] == 'Income')
    total_expense = sum(t['amount'] for t in transactions.values() if t['type'] == 'Expense')
    balance = total_income - total_expense
    return total_income, total_expense, balance

def view_summary(transactions):
    """Displays all transactions and the current financial summary."""
    if not transactions:
        print("\n😔 No transactions recorded yet.")
        return

    total_income, total_expense, balance = calculate_balance(transactions)

    # --- Print Transactions ---
    print("\n" + "="*40)
    print("       Transaction History ")
    print("="*40)
    
    # Sort by ID (effectively by date added) for chronological view
    sorted_ids = sorted(transactions.keys())
    
    for tid in sorted_ids:
        t = transactions[tid]
        sign = '+' if t['type'] == 'Income' else '-'
        color = '\033[92m' if t['type'] == 'Income' else '\033[91m' # Green for Income, Red for Expense
        reset = '\033[0m'
        
        print(f"[{t['date'].split(' ')[0]}] {t['description'][:20]:<20} | {color}{sign}${t['amount']:>8.2f}{reset} ({t['type']})")

    # --- Print Summary ---
    print("\n" + "="*40)
    print("          Financial Summary ")
    print("="*40)
    print(f"  Total Income:   ${total_income:10.2f}")
    print(f"  Total Expense: -${total_expense:10.2f}")
    print("-" * 27)
    # Highlight balance with color
    balance_color = '\033[92m' if balance >= 0 else '\033[91m'
    print(f"  Current Balance: {balance_color}${balance:10.2f}{reset}")
    print("="*40)


def main():
    """Main function to run the expense manager application loop."""
    # This dictionary will hold all our transactions
    # Key: Transaction ID (int), Value: Transaction details (dict)
    transactions_db = {} 

    print(" Welcome to the Simple Expense Manager! ")

    while True:
        print("\n--- Menu ---")
        print("1. Add **Income**")
        print("2. Add **Expense**")
        print("3. View **Summary** & History")
        print("4. **Exit**")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1' or choice == '2':
            # Get transaction details
            trans_type = 'Income' if choice == '1' else 'Expense'
            amount = input(f"Enter {trans_type} amount: $")
            description = input(f"Enter description for {trans_type}: ")
            add_transaction(transactions_db, trans_type, amount, description)

        elif choice == '3':
            view_summary(transactions_db)

        elif choice == '4':
            print("\n👋 Thank you for using the Expense Manager. Goodbye!")
            break

        else:
            print("\n⚠️ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

