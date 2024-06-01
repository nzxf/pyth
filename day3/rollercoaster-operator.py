print("Welcome to the rollercoaster!")

height = int(input("What is your height in centimeter?" ))

if height > 120:
    print("You can ride the rollercoaster!")
    # TICKET PRICE BASED ON AGE
    age = int(input("What is your age?" ))
    if age < 12:
        ticket_type = "Child"
        bill = 5
    elif age <= 18:
        ticket_type =  "Youth"
        bill = 7
    elif age >= 45 and age <= 55:
        ticket_type = "Special Promo"
    else:
        ticket_type = "Adult"
        bill = 12
    # OPTIONAL: ADD PHOTO BILL
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        print(f"{ticket_type} tickets are ${bill}. Plus photo, your total will be ${bill+3}")
    else: 
        print(f"{ticket_type} tickets are ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")