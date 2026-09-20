def ticket_sales():
    Total_Tickets = 10
    Total_Sales = 0

    print("Total Remaining Tickets: (Ticket_Seller)")
    print("Maximum 4 Tickets Per Person.")


    while Total_Tickets > 0:
        print(f"Remaning Buyable Tickets: {Total_Tickets}")

        try:
            Ticket_Seller = int(input("Please input how many tickets you would like to buy between 1-4"))
            if Ticket_Seller <= 0:
                print("Please Have an input of atleast 1 to proceed")
                continue

            if Ticket_Seller > 4:
                print("Sorry you can only buy 4 tickets")
                continue

            if Ticket_Seller > Total_Tickets:
                print(f"Sorry we only have {Total_Tickets} tickets remaining")
                continue

            Total_Tickets -= Ticket_Seller
            Total_Sales += 1
            print(f"Buying {Ticket_Seller} tickets now")

        except ValueError:
            print("Please Enter a valid number")

    print("Tickets Sold Out")
    print(f"Total Buyers: {Total_Sales}")

if __name__ == "__main__":
    ticket_sales()
