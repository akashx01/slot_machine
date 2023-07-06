import random #it genrate random no.

MAX_LINES = 3 # WE ARE DECLARING THIS HERE SO THAT WE CAN USE IT ANYWHERE IN THE PROGRAM
MAX_BET = 100
MIN_BET = 1

ROWS = 3 #it specifies how many rows are in their
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
        
    return winnings,winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols =  all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns  

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")    
        print()
        
def deposit(): #responsible for collecting user deposit
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #check if the value enterd is number or not
            amount = int(amount) #convert the value into int bcz by default its string
            if amount > 0: #if amt>0 break out from the loop
                break
            else:    #if its not then print this stmnt
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #check if the value enterd is number or not
            lines = int(lines) #convert the value into int bcz by default its string
            if 1 <= lines <= MAX_LINES: #CHECK THE VALUES THAT IT IS IN BWTWEEN LINES
                break
            else:    #if its not then print this stmnt
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet(): #define a fnc for the betting amnt
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #check if the value enterd is number or not
            amount = int(amount) #convert the value into int bcz by default its string
            if MIN_BET <= amount <= MAX_BET: #if amt>min_bet and less than or equal t max_bet
                break
            else:    #if its not then print this stmnt
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount 

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
         
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
          
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on lines", *winning_lines)  
    return winnings - total_bet 


def main():  #define main fnc.
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")
  
main()
    
