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
       1. "Which sentence is correctly written?"
            a. Why he didn't go to the library yesterday?
            b. Why did'nt he go to the library yesterday?
            c. Why didn't he go to the library yesterday?
            d. Why didn't he went to the library yesterday?
           answer: b
       2. "Which sentence avoids a dangling modifier?"
            a. Having finished the lab report, the laptop was finally closed.
            b. While peering through the microscope, the cells were clearly visible.
            c. After reading the research paper, the student finally understood the hypothesis.
            d. To improve your grades, the textbook must be read daily.
           answer: c
       3. "Which sentence correctly uses the subjunctive mood to express a wish or hypothetical?"
            a. I wish I was able to attend the conference last Friday.
            b. If the experiment were to fail, we would need to restart the data collection.
            c. It is essential that he arrives before the bell rings
            d. The teacher requested that every student is on time.
           answer: b
       4. "Which sentence uses 'whom' correctly in an objective case?"
            a. Whom do you think will win the science fair?
            b. I don't care whom is going to the gala.
            c. The student whom wrote the winning essay is in my class.
            d. For whom was the scholarship fund established?
           answer: d
       5. "Which sentence is an example of a Strawman fallacy?"
            a. Either study for ten hours or prepare to fail the exam.
            b. If we miss one deadline, we will all fail the entire year.
            c. You want less homework? You clearly want us to be uneducated.
            d. Don't listen to his stories; he's a known liar.
           answer: c
       6. "Which sentence is an example of a Ad Hominem fallacy?"
            a. The plane is bad because it will cost too much money.
            b. We should reject his essay because he is a lazy student.
            c. If you eat one candy, you will lose all of your teeth.
            d. Why talk about grades when the gym is in such a bad shape?
           answer: b
       7. "Which sentence is an example of a Slippery Slope Fallacy?"
            a. Do you want to go to the park or stay home and rot?
            b. If we let him in late, soon thw whole city will be in chaos.
            c. You don't like the food? You must want us all to starve.
            d. He is a bad person, so his advice on health is wrong.
           answer: b
       8. "Which sentence uses the word 'its' or 'it's' correctly?"
            a. The cat licked it's paw after eating the bowl of fish.
            b. I think its going to be a very long day in the laboratory.
            c. The robot moved its arm to pick uo the small metal bolt.
            d. 
           answer: c
       9. ""
            a.
            b.
            c.
            d.
           answer: a
       10. ""
            a.
            b.
            c.
            d.
           answer: d
    # MATH
       1. ""
            a.
            b.
            c.
            d.
           answer: 
       2. ""
            a.
            b.
            c.
            d.
           answer: 
       3. ""
            a.
            b.
            c.
            d.
           answer: 
       4. ""
            a.
            b.
            c.
            d.
           answer: 
       5. ""
            a.
            b.
            c.
            d.
           answer: 
       6. ""
            a.
            b.
            c.
            d.
           answer: 
       7. ""
            a.
            b.
            c.
            d.
           answer: 
       8. ""
            a.
            b.
            c.
            d.
           answer: 
       9. ""
            a.
            b.
            c.
            d.
            answer: 
       10. ""
            a.
            b.
            c.
            d.
           answer: 
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
                a. It increases the speed of the winds near the equator
                b. It deflects the path of the winds to the left
                c. It deflects the path of the winds to the right
                d. It causes the winds to move in a vertical line
            answer: c
       # P6
            1. "Who is the father of electricity?"
                a. Michael Faraday
                b. Thomas Edison
                c. Nikola Tesla
                d. Benjamin Franklin
            answer: a
            2. ""
            answer: a
       # CHEM
            1. "Which of the following intermolecular forces is the strongest?"
                a. London dispersion forces
                b. Dipole-dipole interactions
                c. Hydrogen bonding
                d. Ion-induced dipole forces
            answer: d
            2. "Using VSEPR theory, what is the molecular geometry of SF4"
                a. Tetrahedral
                b. Trigonal pyramidal
                c. See-saw
                d. Square planar
            answer: a
            3. "What is the half-life of a 100g radioactive sample if only 12.5g remains after 30 days?"
                a. 5 days
                b. 10 days
                c. 15 days
                d. 20 days
            answer: b
