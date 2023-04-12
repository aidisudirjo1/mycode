
#!/usr/bin/env python3
"""Work with if, elif, else & while"""

round = 0
answer = " "

while round < 3 and answer.lower() != "brian":
    round = round + 1
    print("Finish the movie title, 'Monty Python\'s The Life of _____'")
    answer = input("Your guess--> ")

    if answer.lower()  == 'brian':
        print("Correct")
        
    elif round==3:
        print("Sorry, the answer was Brian.")
        
    else:
        print("Sorry, try again")



