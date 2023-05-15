# The application re-serves the menu after interface executions
def keep_going():
    keep_going = input('Would you like to make another transaction? select y or n: ')
    if keep_going == 'y':
        main()
    if keep_going == 'n':
        exit_option()

import json

def close_ledger(acct_balance):
     with open('ledger.txt', 'w') as nb:
        json.dump(acct_balance, nb) 

# The transactions effect a balance that is saved to a ledger file.
# The user is able to view the balance appropriately
def balance_option(acct_balance):
    print(f'Your balance is $ {acct_balance}')
    keep_going()
   # print(acct_balance)
       
# The crediting option of the application operates appropriately
def credit_option(acct_balance):
    credit_input = input('How much would you like to credit this account: $')
    acct_balance = float(acct_balance) + float(credit_input)
    print(f'Your new balance after credit is: $ {acct_balance}')
    close_ledger(acct_balance)
    keep_going()
    return acct_balance

# The debit option of the application operates appropriately
def debit_option(acct_balance):
    debit_input = input ('How much would you like to withdraw: $')
    acct_balance = float(acct_balance) - float(debit_input)
    print(f'Your new balance after debit is: $ {acct_balance}')
    close_ledger(acct_balance)
    keep_going()
    return acct_balance

#The checkbook application can be closed appropriately
def exit_option():
    exit_input = input('Are you sure you want to exit? select y or n:')
    if exit_input == 'y':
        print(f'Thank you and Goodbye!')
    elif exit_input == 'n':
        print('You will be returned to the main screen')
        main()
    else:
        print('That is an invalid input. Please select y or n:')

#View Balance, Credit, Debit, and Exit
# #1. Basic functionality
# # application opens interface 4 opts. The transaction with balance saved file

def main():
    ledger = open('ledger.txt')
    acct_balance = ledger.read()
    
    print('\n\nWelcome to the Bank of Carter! \nPlease type option from the menu as prompted \nor you will be removed from the bank? \n\n')
    print('balance\ncredit\ndebit\nexit\n')



    balance = 'Balance'
    credit = 'Credit'
    debit = 'Debit '
    exit_checkbook = 'Exit'

    choice = input()

    if choice == 'balance':
        print( 'You selected balance')
        balance_option(acct_balance)
    elif choice == 'credit':
        print('You selected credit')
        credit_option(acct_balance)
    elif choice == 'debit':
        print('You selected debit')
        debit_option(acct_balance)
    elif choice == 'exit':
        print('You selected exit checkbook')
        exit_option()
    else:
        print('That is an invalid input. Please select y or n:')
    # close_ledger()

main()