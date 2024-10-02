print("Hello welcome to The Secret Auction Program")

bid_info = {}

def run_program():
    name = input("Enter You Code name: ")

    bid_amount = int(input("Enter Bid amount: "))

    bid_info[name] = {"bid": 0}
    bid_info[name]["bid"] = bid_amount

    print(f"Anonymos {name} has bid ₦{bid_amount}")



def exit_program():
    max_value = max(bid_info)

    print(max_value)

    

while True:
    option = int(input(f"Would you like to be \n1. Yes \n2. No \nSelect Option 1 or 2: "))

    match option:
        case 1:
            run_program()
        case 2:
            exit_program()
            print(bid_info)
            print("Exiting Program")
            break
        case _:
            print("Invlid option select either 1 or 2")

