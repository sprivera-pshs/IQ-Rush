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
       print("ERROR: Subject already completed or invalid input.")

# question ideas
    # ENGLISH
       1.
       2.
       3.
       4.
       5.
       6.
       7.
       8.
       9.
       10.
    # MATH
       1.
       2.
       3.
       4.
       5.
       6.
       7.
       8.
       9.
       10.
    # SCIENCE
       # BIO
            1. "What organelle is responsible for producing energy in a cell?"
                a. Mitochondira
                b. Vacuole
                c. Ribosomes
                d. Golgi apparatus
           answer: a
            2. "Which of these statements correctly differentiates obligate anaerobes and facultative anaerobes?"
                "I. Obligate anaerobes cannot live in oxygen but facultative anaerobes can.
                II. Both groups perform aerobic respiration when O2 is present.
                III. Facultative anaerobes rely on fermentation even in the presence of O2.
                IV. Obligate anaerobes lack ROS-detoxifying enzymes but facultative anaerobes have them."
                a. I and IV
                b. II and IV
                c. I and II
                d. III and IV
            answer: a
            3. "Which of the following BEST describes the function of smooth endoplasmic reticulum"
                a. The smooth endoplasmic reticulum detoxifes harmful substances in cells.
                b. The smooth endoplasmic reticulum produces lipids and steroid hormones.
                c. The smooth endoplasmic reticulum stores and releases calcium ions.
                d. The smooth endoplasmic reticulum is studded with ribosomes for protein synthesis.
            answer: b
       # ES
            1. "Which seismic waves cause the most surface destruction during an earthquake?"
                a. P-waves produce rolling motion along the ground surface during an earthquake.
                b. Rayleigh waves only move thrpugh the deepest parts of the Earth duuring an earthquake.
                c. Surface waves cause the strongest ground movement during an earthquake.
                d. Love waves travel fastest thru the Earth's interior during an earthquake.
            answer: c
            2. "How does the Coriolis effect influence wind patterns in the Northern Hemisphere?"
                a.
                b.
                c.
                d.
       # P6
            1. ""
            2. ""
       # CHEM
            1. "Which of the following intermolecular forces is the strongest?"
                a. London dispersion forces
                b. Dipole-dipole interactions
                c. Hydrogen bonding
                d. Ion-induced dipole forces
            2. "Using VSEPR theory, what is the molecular geometry of SF4"
                a. Tetrahedral
                b. Trigonal pyramidal
                c. See-saw
                d. Square planar
            3. ""
