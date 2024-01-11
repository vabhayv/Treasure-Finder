print("Welcome to the Treasure Finder\n Your mission is to find the treasure!!!")
first=input("There are two ways to go Left or Right. Make your decision!\n(write left or right)")
lower_first = first.lower()
if lower_first == "left":
    second = input("There is a lake, what you'll do? Swim or Wait? make your decision!\n(write Swim or Wait)")
    lower_second = second.lower()
    if lower_second == "wait":
        third = input("There are three houses red, blue and green!! Which one you'll choose?\n(write red or blue or green)")
        lower_third = third.lower()
        if lower_third == "blue":
            print("Congratulations You Find The Treasure")
        elif lower_third == "red":
            print("There was a time bomb, you loose\nTry again")
        else :
            print("someone locked you in that house. start from the beginning")
    elif lower_second == "swim":
        print("there was crocodile in the lake, you loose")
elif lower_first == "right":
    print("That was the dead end!!")
