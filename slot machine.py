MAX_LINES =3



def deposit():
    while True:
        amount = input('what would you like to deposit ? $')
        if amount.isdigit():
            amount=int(amount)
            amount=int(amount)
            if amount> 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount
def main():
    balance = deposit()

main( )

def get_number_of_lines():
    while True:
       lines= input("enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
       if lines.isdigit():
            lines=int(lines)

            if 1 <=lines <=MAX_LINES:
                 break


            else:
                print("amount must be greater than 0.")
    else:
            print("please enter a number.")

    return Lines

def main():
    balance = deposit()
    lines=get_number_of_lines()
    print(balance, lines)

main( )