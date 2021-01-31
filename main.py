import datetime
import random

def answer_log(numbers):
    listing.append(numbers)
    

def wrong_answer(wrong):
    
    # date_wrong = date.today()
    listing.append(wrong)
    print(listing)
    # This will go to a database instead of a list?

    
def mike():
    global listing
    listing = []
    times = 4
    i = 0
    q = 0
    while i <= times:
        print(i+1)
        
        ######## Checking to see if input is number ######
        while True:
            try:
                a = int(input("pick a number "))
            except ValueError:
                print("Please enter a number 1-9")
                mike()
            else:
                break
        ##################################################
        
        b = random.randint(1, 10)
        answer = a * b
        answer_log(f'{a} * {b} = ')
        c = int(input(f"What is?  {a} * {b}: "))
        if c == answer:
            print(f"Correct! {a} * {b} is { answer }")
        else:
            print(f"Incorrect! {a} * {b} is { answer }")
            wrong_answer(f'{a} * {b} = {c} WRONG')
            
            print(f'Lets practice! {a} * {b} = {answer}')
            while q <= 3:
                
                c = int(input(f"What is?  {a} * {b}: "))
                if c == answer:
                    print("Good")
                else:
                    print("Practice!")
                q += 1
            print("------#####------\n Lets continue")
        i += 1
        
    print("-----------ooo------------")
    for p in listing:
        print(p)


mike()