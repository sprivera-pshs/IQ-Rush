# English quiz function
def englishQuiz():
    english_score = 0

    print("--- English Category ---")

    print("\nWhat are at least 3 elements of a short story?")
    print("A. Plot, Conflict, Rising Action")
    print("B. Plot, Cosmopolitan, Rising Action")
    print("C. Marvel, Conflict, Rising Action")
    print("D. Plot, Caipirinha, Rhubarb")
    answer = input("Input your answer here (capital): ")
    correct_answer = "A"

    if answer == correct_answer:
        english_score += 1
        print(f"Correct! You currently have {english_score} point.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {english_score}.")

    return english_score

# Math quiz function
def mathQuiz():

    math_score = 0

    print("--- Math Category ---")

    print("\nQ1. Simplify cube root of 125. ")
    print("A. 6")
    print("B. 5")
    print("C. 7")
    print("D. 5.4")
    answer = input("Input your answer here (capital): ")
    correct_answer = "B"

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

    print("\nQ1: What part of the cell controls its activities? ")
    print("A. Cytoplasm")
    print("B. Mitochondria")
    print("C. Nucleus")
    print("D. Ribosome")
    answer = input("Input your answer here (capital): ")
    correct_answer = "C"

    if answer == correct_answer:
        science_score = science_score + 1
        print(f"Correct! You currently have {science_score} point.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {science_score}.")

    return science_score

# Menu
leaderboard = {} #initialization
gameIteration = False
engDone = False
mathDone = False
sciDone = False
player_name = input("Please enter your name: ")

while gameIteration == False:
   print("--- IQ RUSH HUB ---")
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
        print("Science: Physics, Earth Science.")
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
       print("ERROR: Subject already completed or invalid input.")
