from random import randint
while True:
    random_number = randint(1,10)
    #print(random_number)
    for i in range(3,0,-1):
        user_input = int(input(f"Give me a number between 1-10, you have {i} possibilities left\n"))
        if random_number != user_input and i == 1:
            print("No luck")
        elif random_number != user_input:
            print("No, try again")
            continue
        else :
            print(f"Congrats, the number was {random_number}")
            break
    more = input("Do you want to play more?(y/hit any key)")
    if more.lower() == 'y':
        continue
    else:
        print("Thank you for playing, bye")
        break