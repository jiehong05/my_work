
from datetime import datetime
import math

# Enhancement: track total transactions and transaction log
total_transactions = 0
transaction_log = []

def menu():
    print('''
------------------------------------------------------------
Welcome to Parking Fee Calculator
------------------------------------------------------------

1. Display Rate Table
2. Parking Fee Calculator
3. View Transaction Summary
4. Help

0. Exit
''')

def option_1():
    print('''
RATE TABLE

Type 1: Short Term Car Park (Block A, B, C & D)
1st - 3rd hour             RM 5.00 / hour
4th - 5th hour             RM 4.00 / hour
6th - 10th hour            RM 3.00 / hour
11th - 17th hour           RM 2.00 / hour
Maximum rate per day       RM 52.00

Type 2: Preferred Parking (Block B & C Level 2)
1st - 6th hour             RM 6.00 / hour
7th - 24th hour            RM 5.00 / hour
Maximum rate per day       RM123.00

Type 3: Long Term Car Park (Block C & D)
1st - 4th hour             RM 3.00 / hour
5th - 14th hour            RM 2.00 / hour
Maximum rate per day       RM 32.00

Type 4: Long Term Car Park (Block A & B)
Day 1 - Day 3              RM 52.00 / day
Day 4 & onwards            RM 30.00 / day

Type 5: Parking E
1st - 3rd hour             RM 4.00 / hour
4th - 9th hour             RM 3.00 / hour
10th - 15th hour           RM 2.00 / hour
16th - 18th hour           RM 1.50 / hour
Maximum rate per day       RM 42.00
''')

def get_validated_input(prompt):
    datetime_format = "%d/%m/%y %H:%M:%S"
    while True:
        user_input = input(prompt)
        try:
            return datetime.strptime(user_input, datetime_format)
        except ValueError:
            print("Invalid format! Please use the format dd/mm/yy HH:MM:SS")

def calculate_hours_days(start_time, end_time):
    duration = end_time - start_time
    total_hours = math.ceil(duration.total_seconds() / 3600)
    total_days = duration.days
    print(f"Total parking time: {total_days} day(s) and {total_hours} hour(s)")
    return total_hours, total_days

# Define fee calculators for each type
def type_1(num, day):
    if 0 <= num <= 3 and day == 0:
        total = num * 5
    elif 4 <= num <= 5 and day == 0:
        total = 3 * 5 + (num - 3) * 4
    elif 6 <= num <= 10 and day == 0:
        total = 3 * 5 + 2 * 4 + (num - 5) * 3
    elif 11 <= num <= 17 and day == 0:
        total = 3 * 5 + 2 * 4 + 5 * 3 + (num - 10) * 2
    elif num >= 18 and day == 0:
        total = 52
    else:
        total = type_1(num, 0) + day * 52
    return total

def type_2(num, day):
    if 0 <= num <= 6 and day == 0:
        total = num * 6
    elif 7 <= num <= 23 and day == 0:
        total = 6 * 6 + (num - 6) * 5
    elif num >= 24 and day == 0:
        total = 123
    else:
        total = type_2(num, 0) + day * 123
    return total

def type_3(num, day):
    if 0 <= num <= 4 and day == 0:
        total = num * 3
    elif 5 <= num <= 14 and day == 0:
        total = 4 * 3 + (num - 4) * 2
    elif num >= 15 and day == 0:
        total = 32
    else:
        total = type_3(num, 0) + day * 32
    return total

def type_4(num, day):
    if 0 < num and 1 <= day <= 3:
        total = (day + 1) * 52
    elif num == 0 and 1 <= day <= 3:
        total = day * 52
    elif 0 < num and day > 3:
        total = 3 * 52 + (day - 3 + 1) * 30
    elif num == 0 and day > 3:
        total = 3 * 52 + (day - 3) * 30
    else:
        total = 52 if day == 0 else day * 52
    return total

def type_5(num, day):
    if 0 <= num <= 3 and day == 0:
        total = num * 4
    elif 4 <= num <= 9 and day == 0:
        total = 3 * 4 + (num - 3) * 3
    elif 10 <= num <= 15 and day == 0:
        total = 3 * 4 + 6 * 3 + (num - 9) * 2
    elif 16 <= num <= 18 and day == 0:
        total = 3 * 4 + 6 * 3 + 6 * 2 + (num - 15) * 1.5
    elif num >= 19 and day == 0:
        total = 42
    else:
        total = type_5(num, 0) + day * 42
    return total

def calculate_fee_by_type(num, day, parking_type):
    if parking_type == '1':
        return type_1(num, day), "Short Term Car Park (Block A, B, C & D)"
    elif parking_type == '2':
        return type_2(num, day), "Preferred Parking (Block B & C Level 2)"
    elif parking_type == '3':
        return type_3(num, day), "Long Term Car Park (Block C & D)"
    elif parking_type == '4':
        return type_4(num, day), "Long Term Car Park (Block A & B)"
    elif parking_type == '5':
        return type_5(num, day), "Parking E"
    else:
        return None, None

def process_payment(fee):
    print('''
------------------------------------------------------------
Parking Payment Option
------------------------------------------------------------
1. Cash 
2. Debit Card / Credit Card
3. E-Wallet
------------------------------------------------------------
''')
    while True:
        option = input("Choose a payment option (1 - 3): ")
        if option == '1':
            return "Cash"
        elif option == '2':
            return "Debit Card / Credit Card"
        elif option == '3':
            return "E-Wallet"
        else:
            print("Please choose a valid option (1,2,3)")

def display_help():
    print('''
FAQ

Please contact 010-378 2645 for further inquiries. Thank you.
''')

def exit_menu():
    while True:
        op_0 = input("Are you sure you want to exit? (1: Yes / 2: No): ")
        if op_0 == '1':
            print("Thank you for visiting. Please come again.")
            exit()
        elif op_0 == '2':
            break
        else:
            print("Please choose a valid option (1,2)")

def display_summary():
    print("\n===== Transaction Summary =====")
    print(f"Total Transactions: {total_transactions}")
    for i, txn in enumerate(transaction_log, 1):
        print(f"{i}. {txn['location']} | RM{txn['fee']:.2f} | {txn['payment_method']}")

# Main loop
def run_program():
    global total_transactions, transaction_log

    while True:
        menu()
        option = input("Choose an option: ")

        if option == '1':
            option_1()

        elif option == '2':
            start_time = get_validated_input("Start (dd/mm/yy HH:MM:SS): ")
            end_time = get_validated_input("End   (dd/mm/yy HH:MM:SS): ")
            while end_time <= start_time:
                print("End time must be after start time.")
                end_time = get_validated_input("Re-enter end time: ")

            total_hours, total_days = calculate_hours_days(start_time, end_time)
            option_1()
            while True:
                p_type = input("Choose a parking type (1-5): ")
                fee, location = calculate_fee_by_type(total_hours, total_days, p_type)
                if fee is not None:
                    break
                print("Invalid parking type. Please try again.")

            print(f"\nYou selected: {location}\nYour fee is: RM{fee:.2f}")
            payment_method = process_payment(fee)

            total_transactions += 1
            transaction_log.append({
                "location": location,
                "fee": fee,
                "payment_method": payment_method
            })

            print("\nPayment Successful!")
            print(f"Location       : {location}")
            print(f"Total Fee      : RM{fee:.2f}")
            print(f"Payment Method : {payment_method}")
            print("Thank you. Please come again.")

        elif option == '3':
            display_summary()

        elif option == '4':
            display_help()

        elif option == '0':
            exit_menu()

        else:
            print("Invalid option. Please choose 0 - 4.")

run_program()
