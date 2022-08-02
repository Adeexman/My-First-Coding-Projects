# Building a guessing game using if statement and while loop

print("Are you ready to play this game?")
print("Attention: Your response is case sensitive. Write all your responses in small letters")
Response = "yes"
Answer = ""
Answer = input("Enter your answer:")
if Answer == Response:
    print("Welcome to the intelligence test!\n Let's begin")

    print("Q1: What has to be broken off before you use it?")
    Response = "egg"
    Answer = ""
    Answer = input("Enter your answer:")
    while Answer != Response:
        Answer = input("Try again:")
    print("Good Job, Keep it up!")

    print("Q2: When I am young, I am tall, when I am old I become short!")
    Response = "candle"
    Answer = ""
    Answer = input("Enter your answer:")
    while Answer != Response:
        Answer = input("Try again:")
    print("Great Job!")

else:
    print("Don't give up, this is a chance to boost your intelligence!\n Would you like to give it a try?")
    Response = "yes"
    Answer = ""
    Answer = input("Enter your response:")
    if Answer == Response:
        print("Welcome to the intelligence test!\nLet's begin")

        print("Q1: What has to be broken off before you use it?")
        Response = "egg"
        Answer = ""
        Answer = input("Enter your answer:")
        while Answer != Response:
            Answer = input("Try again:")
        print("Good Job, Keep it up!")

        print("Q2: When I am young, I am tall, when I am old I become short!")
        Response = "candle"
        Answer = ""
        Answer = input("Enter your answer:")
        while Answer != Response:
            Answer = input("Try again:")
        print("Great Job!")

    else :
        print("Goodluck with your life!")