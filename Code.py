import json

# Specify the filename
filename = "my_data.json"

with open('my_data.json', 'r') as file:
    data = json.load(file)

# English quiz function
def englishQuiz():
    english_score = 0
    print("\n--- English Category ---")

    for item in data["engQuestions"]:
        question_text = list(item.values())[0]
        print(question_text)
        answer = input("Input your answer here: ").upper()
        correct_answer = item["choice"]

        if answer == correct_answer:
            english_score += 1
            print(f"Correct! You currently have {english_score} point.")
        else:
            print(f"Incorrect! The right answer was {answer} You currently have {english_score}.")
        print("")

    return english_score

# Math quiz function
def mathQuiz():
    math_score = 0
    print("--- Math Category ---")

    for item in data["mathQuestions"]:
        question_text = list(item.values())[0]
        print(question_text)
        answer = input("Input your answer here: ").upper()
        correct_answer = item["choice"]

    if answer == correct_answer:
        math_score = math_score + 1
        print(f"Correct! You currently have {math_score} point.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {math_score}.")

    return math_score

# Science quiz function
def scienceQuiz():
    science_score = 0
    print("--- Science Category ---")

    for item in data["sciQuestions"]:
        question_text = list(item.values())[0]
        print(question_text)
        answer = input("Input your answer here: ").upper()
        correct_answer = item["choice"]

    if answer == correct_answer:
        science_score = science_score + 1
        print(f"Correct! You currently have {science_score} point.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {science_score}.")

    print(f"\nNice one! You got {science_score}! ")

    return science_score

# Menu
leaderboard = {} #initialization
gameIteration = False
engDone = False
mathDone = False
sciDone = False
player_name = input("Please enter your name: ")
print(f"\nHi, {player_name}! Welcome to IQ Rush!")

while gameIteration == False:
   print("\n--- IQ RUSH HUB ---")
   print("0: How to Play & About Subjects")
   print("1: English")
   print("2: Math")
   print("3: Science")
   print("4: Done (Finish Game)")
   select = int(input("Please input your choice: "))

   if select == 0:
        print("\n--- HOW TO PLAY ---")
        print("1. Choose a subject by typing its number (1, 2, or 3).")
        print("2. Answer questions using CAPITAL letters only (A, B, C, or D).")
        print("3. Each correct answer earns you 1 point.")
        print("4. You must complete ALL subjects to finish the game.")
        print("\n--- ABOUT THE SUBJECTS ---")
        print("English: Story elements and metaphors.")
        print("Math: Radicals and square roots.")
        print("Science: Physics, Earth Science, Biology.")
        print()

   elif select == 1 and engDone == False:
        engScore = englishQuiz()
        engDone = True

   elif select == 2 and mathDone == False:
        mathScore = mathQuiz()
        mathDone = True

   elif select == 3 and sciDone == False:
        sciScore = scienceQuiz()
        sciDone = True

# ending the game + leaderboard
   elif select == 4:
        if engDone and mathDone and sciDone:
            avgScore = (engScore + mathScore + sciScore) / 3
            leaderboard[player_name] = avgScore
            print(f"\nGame finished! Your average score is {avgScore:.2f}")

            print("\n--- LEADERBOARD ---")
            sortedLeaderboard = sorted(leaderboard, key=leaderboard.get, reverse=True)
            for p in sortedLeaderboard:
                print(p, "-", leaderboard[p])
            gameIteration = True

        else:
           print("ACCESS DENIED: You must complete all subjects first!")
   else:
       print("")
       print("-" * 50)
       print("\nERROR: Subject already completed or invalid input.")
       print("")
       print("-" * 50)
