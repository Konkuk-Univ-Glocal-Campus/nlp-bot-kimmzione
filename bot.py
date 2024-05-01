import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I am Marvin, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
        # Translate English responses into Korean
        if response == "That is quite interesting, please tell me more.":
            response = "매우 흥미로워요. 더 말해주세요."
        elif response == "I see. Do go on.":
            response = "알겠어요. 계속 이야기해 주세요."
        elif response == "Why do you say that?":
            response = "왜 그러시나요?"
        elif response == "Funny weather we've been having, isn't it?":
            response = "요즘 날씨가 참 재미있네요, 안 그래요?"
        elif response == "Let's change the subject.":
            response = "주제를 바꿔볼까요?"
        elif response == "Did you catch the game last night?":
            response = "어젯밤 경기 보셨어요?"
    print(response)

print("It was nice talking to you, goodbye!")

