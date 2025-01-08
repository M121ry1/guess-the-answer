#Pythonn ques game:
question = ("How many elements are in the periodic table?:",
            "which animal lays the largest eggs?:",
            "What is the most aboundant gas in Earth's atmosphere?:",
            "How many bones are in the human body ?:",
            "Which planet in the solar system is the hottest?:")

options = (("A. 116","B. 117 ","C. 118 ","D. 119 "),
          ("A. Whale ","B. Crocodile ","C. Elephant ","D. Ostrich "),
          ("A. Nitrogen ","B. Oxigen ","C. Carbon -Dioxide ","D. Hydrogen "),
          ("A. 206 ","B. 207 ","C. 208 ","D. 209 "),
          ("A. Mercury ","B. Venus ","C. Earth ","D. Mars "))



answers = ("C","D","A","A","B")

guesses = []
score = 0
question_num = 0
for question in question:
    print("........................")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 2
            print("CORRECT!")
    else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answers")
            
    question_num += 1


print("......................")
print("        RESULTS       ")
print("......................")

print("answer: ",end="")
for answer in answers:
    print(answer,end= " ")
print()

print("gesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(question)*100

print(score)
