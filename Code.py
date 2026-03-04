def englishQuiz():
    english_score = 0

    print("--- English Category ---")

    answer = input("Q1: What are at least 3 elements of a short story? ")
    correct_answer = "A"

    if answer == correct_answer:
        score += 1
        print(f"Correct! You currently have {english_score}.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {english_score}.")

    return english_score
#hello




def mathQuiz():

    math_score = 0

    print("--- Math Category ---")

    answer = input("Q1. What is the Simplify cube root of 125.")
    correct_answer = "B"

    if answer == correct_answer:
        math_score = math_score + 1
        print(f"Correct! You currently have {math_score}.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {math_score}.")

    return math_score






def scienceQuiz():


    science_score = 0


    print("--- Math Category ---")


    answer = input("Q1: What part of the cell controls its activities?")
    correct_answer = "C"


    if answer == correct_answer:
        science_score = science_score + 1
        print(f"Correct! You currently have {science_score}.")
    else:
        print(f"Incorrect! The right answer was {answer} You currently have {science_score}.")


    return science_score


gameIteration = False
while gameIteration == False:
   print("--- IQ RUSH HUB ---")
   print("0: How to Play & About Subjects")
   print("1: English")
   print("2: Math")
   print("3: Science")
   print("4: Done (Finish Game)")
   select = int(input("Please input your choice: "))




   if select == 0:
        print("--- HOW TO PLAY ---")
        print("1. Choose a subject by typing its number (1, 2, or 3).")
        print("2. Answer questions using CAPITAL letters only (A, B, C, or D).")
        print("3. Each correct answer earns you 1 point.")
        print("4. You must complete ALL subjects to finish the game.")
        print("\n--- ABOUT THE SUBJECTS ---")
        print("English: Story elements and metaphors.")
        print("Math: Radicals and square roots.")
        print("Science: Physics, Earth Science.")


   elif select == 1 and engDone == False:
        engScore = englishQuiz()
        engDone = True


   elif select == 2 and mathDone == False:
        mathScore = mathQuiz()
        mathDone = True


   elif select == 3 and sciDone == False:
        sciScore = scienceQuiz()
        sciDone = True


   elif select == 4:
        if engDone and mathDone and sciDone:
           gameIteration = True
        else:
           print("ACCESS DENIED: You must complete all subjects first!")
   else:
       print("ERROR: Subject already completed or invalid input.")
