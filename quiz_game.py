def new_game():
    guesses = []
    correct_guesses = 0
    ques_number = 1

    for key in questions:
        print(key)
    
    for i in options[ques_number-1]:
        print(i)
        guess = input("Enter (A, B,C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        ques_number += 1

    display_score(correct_guesses,guess)

def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score():
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")

    print("ANSWERS:",end="")
    for i in questions:
        questions.get(i)
        print(i,end="\t")
    print()

    print("GUESSES:",end="")
    for i in guesses:
        print(i,end="\t")
    print()

    score = int(correct_guesses/len(questions))*100
    print(f"TOUR SCORE IS {score}%")

def play_again():
    response = input("DO YOU WANT TO PLAY AGAIN? ").upper()
    if response == "YES":
        return True
    else:
        return False

new_game()

while play_again():
    new_game()

print("BYE....!!! HAVE A NICE DAY :)")

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]