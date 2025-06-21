print("Welcome to the Escrow Wallet System.")

wallet_balance = 0.00
seller_account_balance = 0.00
seller_bank_account = None
buyer_code_part = None
seller_code_part = None

while True:
    print("\nWho are you?")
    print("1. Buyer")
    print("2. Seller")
    print("3. Exit")
    user_type = input("Choose (1-3): ")

    if user_type == "1":
        print("\n--- Buyer Menu ---")
        print("1. Deposit funds")
        print("2. Generate and set release code")
        print("3. Check wallet balance")
        print("4. Exit buyer menu")
        choice = input("Choose (1-4): ")

        if choice == "1":
            amount = input("Enter deposit amount: R")
            try:
                amount = float(amount)
                if amount > 0:
                    wallet_balance += amount
                    print(f" Deposit successful. Wallet now has: R{wallet_balance:.2f}")
                else:
                    print(" Amount must be more than R0.00.")
            except ValueError:
                print(" Invalid input. Please enter a valid number.")

        elif choice == "2":
            full_code = input("Enter a 6-digit release code (numbers only): ").strip()
            if full_code.isdigit() and len(full_code) == 6:
                buyer_code_part = full_code[:3]
                seller_code_part = full_code[3:]
                print(f" Release code set.")
                print(f"Buyer code part: {buyer_code_part}")
                print("Share the seller's 3-digit part with them securely.")
            else:
                print(" Invalid code. Must be exactly 6 digits (e.g. 123456).")

        elif choice == "3":
            print(f" Wallet balance: R{wallet_balance:.2f}")

        elif choice == "4":
            print("Exiting buyer menu.")
        else:
            print(" Invalid option.")

    elif user_type == "2":
        if seller_bank_account is None:
            while True:
                bank_acc = input("Enter your 10-digit personal bank account number: ")
                if bank_acc.isdigit() and len(bank_acc) == 10:
                    seller_bank_account = bank_acc
                    print(" Bank account registered successfully.")
                    break
                else:
                    print(" Invalid input. Bank account number must be exactly 10 digits.")

        print("\n--- Seller Menu ---")
        print(f"Your registered bank account: {seller_bank_account}")
        print("1. Check wallet funds")
        print("2. Release funds with shared code")
        print("3. Check personal account balance")
        print("4. Exit seller menu")
        choice = input("Choose (1-4): ")

        if choice == "1":
            print(f" Wallet currently holds: R{wallet_balance:.2f}")
        elif choice == "2":
            if wallet_balance == 0:
                print(" No funds available to release.")
            elif buyer_code_part is None or seller_code_part is None:
                print(" Buyer has not set a release code yet.")
            else:
                entered_buyer_part = input("Enter buyer's 3-digit code part: ").strip()
                entered_seller_part = input("Enter your 3-digit code part: ").strip()
                if entered_buyer_part == buyer_code_part and entered_seller_part == seller_code_part:
                    seller_account_balance += wallet_balance
                    print(f" Funds released! R{wallet_balance:.2f} sent to your account {seller_bank_account}.")
                    wallet_balance = 0.00
                    buyer_code_part = None
                    seller_code_part = None
                else:
                    print(" Incorrect code combination. Please try again.")
        elif choice == "3":
            print(f" Your personal account balance: R{seller_account_balance:.2f}")
        elif choice == "4":
            print("Exiting seller menu.")
        else:
            print(" Invalid option.")

    elif user_type == "3":
        print("Thank you. Exiting the Escrow Wallet.")
        break
    else:
        print(" Invalid selection.")
