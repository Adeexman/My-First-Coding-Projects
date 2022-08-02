print("This is a riddle game. Are you ready to play, Yes or No?")
print("Attention: Your response is case sensitive. Start all first letter of your response with a capital letter")
Response = "Yes"
Answer = ""
Answer = input("Enter your response: ")
if Answer == Response :
    print("Welcome, lets Begin!")
    print("Q1: I am something full of branches?")
    Response = "Tree"
    Answer = ""
    Answer = input("Enter your response: ")
    while Answer != Response:
        Answer = input("Try again: ")
    print("Good job, you guessed right!")

    print("Q2: What gets wet while drying?")
    Answer = "Towel"
    guess = ""
    guess = input("Enter guess: ")
    while guess != Answer:
        guess = input("Try again:")
    print("Superb")

    print("Q3: I’m tall when I’m young, and I’m short when I’m old. What am I?I")
    Answer = "Candle"
    guess = ""
    guess = input("Enter guess: ")
    while guess != Answer:
        guess = input("Try again:")
    print("Great, you did it again!")

    print("Q4: What can you keep after giving to someone?")
    Answer = "Your word"
    guess = ""
    guess = input("Enter guess: ")
    while guess != Answer:
        guess = input("Try again:")
    print("Fantastic!")
    print("You're almost there, you made it to the last question")

    print("Q5: I have branches, but no fruit, trunk or leaves. What am I?")
    Answer = "Bank"
    guess = ""
    guess = input("Enter guess: ")
    while guess != Answer:
        guess = input("Try again:")
    print("Your brain is fire!")
    print("Keep it up bravo!!!")

elif Answer != Response:
    print("So sad you decided to quit! Will you like to give it a shot?")
    Answer = input("Enter your response: ")
    if Answer == Response:
        print("Great, lets Begin!")
        print("Q1: I am something full of branches?")
        Response = "Tree"
        Answer = ""
        Answer = input("Enter your response: ")
        while Answer != Response:
            Answer = input("Try again: ")
        print("Good job, you guessed right!")

        print("Q2: What gets wet while drying?")
        Answer = "Towel"
        guess = ""
        guess = input("Enter guess: ")
        while guess != Answer:
            guess = input("Try again:")
        print("Superb")

        print("Q3: I’m tall when I’m young, and I’m short when I’m old. What am I?")
        Answer = "Candle"
        guess = ""
        guess = input("Enter guess: ")
        while guess != Answer:
            guess = input("Try again:")
        print("Great, you did it again!")

        print("Q4: What can you keep after giving to someone?")
        Answer = "Your word"
        guess = ""
        guess = input("Enter guess: ")
        while guess != Answer:
            guess = input("Try again:")
        print("Fantastic! You made it to the last question")

        print("Q5: I have branches, but no fruit, trunk or leaves. What am I?")
        Answer = "Bank"
        guess = ""
        guess = input("Enter guess: ")
        while guess != Answer:
            guess = input("Try again:")
        print("Your brain is fire!")
        print("Keep it up bravo!!!")

    elif Answer != Response:
        print("Bye B!!!")
