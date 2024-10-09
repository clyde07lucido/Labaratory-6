print("\nGood Day!")
name = input("What's your name? ")
print(f"\nHello, {name}! Let's Calculate your Registration fee.")

attendee_age = float(input("\nEnter your age: "))
position = input("Are you a Member or Non-Member? (Please type 'Member' or 'Non-Member' only): ")

if attendee_age >= 0 and attendee_age <= 18:
    if position == "Member":
        print(f"Hi, {name}! Your Registration fee is 450.00 pesos")
    elif position == "Non-Member":
        print(f"Hi, {name}! Your Registration fee is 650.00 pesos")
    else:
        print(f"Sorry, {name}. Your Position is invalid")
        
elif attendee_age >=18 and attendee_age <=65:
    if position == "Member":
        print(f"Hi, {name}! Your Registration fee is 550.00 pesos")
    elif position == "Non-Member":
        print(f"Hi, {name}! Your Registration fee is 750.00 pesos")
    else:
        print(f"Sorry, {name}. Your Position is invalid")
        
elif attendee_age >=65 and attendee_age <=120:
    if position == "Member":
        print(f"Hi, {name}! Your Registration fee is 400.00 pesos")
    elif position == "Non-Member":
        print(f"Hi, {name}! Your Registration fee is 600.00 pesos")
    else:
        print(f"Sorry, {name}. Your Position is invalid")
        
else:
    print(f"Sorry, {name}. Your Age is invalid")

    
    
    