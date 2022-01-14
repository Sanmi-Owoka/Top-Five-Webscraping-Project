from framework import Framework


brain = Framework()
is_on = True
while is_on:
    choice = "(Y/N)"
    question = input(f"Would you like to scrape a website {choice}?: ")
    if question.lower() == "y":
        brain.call()
    elif question.lower() == "n":
        print("Thanks for analyzing! Come back again!")
        is_on = False
    else:
        print(f"You entered '{question}', choose either {choice}")