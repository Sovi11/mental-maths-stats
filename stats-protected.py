import time 
import random
import os 

EASY = 1
MEDIUM = 2
HARD = 3
PLUS = 1
MINUS = 2
MULTIPLY = 3

def set_password(username):
    print("Setting password")
    password = input("Enter your password: ")
    file = open("passwords.txt", "a")
    file.write(f"{username} {password}\n")
    file.close()

def initialize_file(file_path):
    file = open(file_path, 'w')
    file.write('Stats :\n')
    file.write('easy + games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('easy - games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('easy * games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('medium + games (num_games, total_time, nuquestions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('medium - games (num_games, total_time, nuquestions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('medium * games (num_games, total_time, nuquestions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('hard + games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('hard - games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.write('hard * games (num_games, total_time, num_questions, correct_questions):\n')
    file.write('0 0 0 0\n')
    file.close()

def start_game(mode, op):
    num_ques = int(input("How many questions do you want to answer? \n"))
    correct = 0
    wrong = 0
    start_time = time.time()
    for i in range(num_ques):
        if mode == EASY:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif mode == MEDIUM:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
        elif mode == HARD:
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
        if op == PLUS:
            ans = a + b
            op_str = "+"
        elif op == MINUS:
            ans = a - b
            op_str = "-"
        elif op == MULTIPLY:
            ans = a * b
            op_str = "*"
        print(f"What is {a} {op_str} {b} ?")
        user_ans = int(input("Your answer: "))
        if user_ans == ans:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! The correct answer is {ans}")
            wrong += 1
    end_time = time.time()
    print(f"Your score: {correct}/{num_ques}")
    print(f"Time taken: {end_time - start_time} seconds")
    print(f"Average time per question: {(end_time - start_time) / num_ques} seconds")
    ask = input("Do you want to put these records in your stats ? (yes/no) \n").strip().lower()
    if ask == "yes":
        file = open(file_path, "r")
        lines = file.readlines()
        file.close()
        file = open(file_path, "w")
        if mode == EASY:
            if op == PLUS:
                lines[2] = f"{int(lines[2].split()[0])+1} {float(lines[2].split()[1])+end_time-start_time} {int(lines[2].split()[2])+num_ques} {int(lines[2].split()[3])+correct}\n"
            elif op == MINUS:
                lines[4] = f"{int(lines[4].split()[0])+1} {float(lines[4].split()[1])+end_time-start_time} {int(lines[4].split()[2])+num_ques} {int(lines[4].split()[3])+correct}\n"
            elif op == MULTIPLY:
                lines[6] = f"{int(lines[6].split()[0])+1} {float(lines[6].split()[1])+end_time-start_time} {int(lines[6].split()[2])+num_ques} {int(lines[6].split()[3])+correct}\n"
        elif mode == MEDIUM:
            if op == PLUS:
                lines[8] = f"{int(lines[8].split()[0])+1} {float(lines[8].split()[1])+end_time-start_time} {int(lines[8].split()[2])+num_ques} {int(lines[8].split()[3])+correct}\n"
            elif op == MINUS:
                lines[10] = f"{int(lines[10].split()[0])+1} {float(lines[10].split()[1])+end_time-start_time} {int(lines[10].split()[2])+num_ques} {int(lines[10].split()[3])+correct}\n"
            elif op == MULTIPLY:
                lines[12] = f"{int(lines[12].split()[0])+1} {float(lines[12].split()[1])+end_time-start_time} {int(lines[12].split()[2])+num_ques} {int(lines[12].split()[3])+correct}\n"
        elif mode == HARD:
            if op == PLUS:
                lines[14] = f"{int(lines[14].split()[0])+1} {float(lines[14].split()[1])+end_time-start_time} {int(lines[14].split()[2])+num_ques} {int(lines[14].split()[3])+correct}\n"
            elif op == MINUS:
                lines[16] = f"{int(lines[16].split()[0])+1} {float(lines[16].split()[1])+end_time-start_time} {int(lines[16].split()[2])+num_ques} {int(lines[16].split()[3])+correct}\n"
            elif op == MULTIPLY:
                lines[18] = f"{int(lines[18].split()[0])+1} {float(lines[18].split()[1])+end_time-start_time} {int(lines[18].split()[2])+num_ques} {int(lines[18].split()[3])+correct}\n"
        file.writelines(lines)
        file.close()
    else:
        print("Your records are not updated")

def game(file_path):
    x =input("Select the difficulty mode : easy , medium , hard\n").strip().lower()
    mode=-1
    op=-1
    if x == "easy":
        print("You have selected easy mode")
        mode=EASY
    elif x == "medium":
        print("You have selected medium mode")
        mode=MEDIUM
    elif x == "hard":
        print("You have selected hard mode")
        mode=HARD
    else:
        print("Invalid input")
        exit()
    x =input("Select the operation mode : + , - , * \n").strip().lower()
    if x == "+":
        print("You have selected addition mode")
        op = PLUS
    elif x == "-":
        print("You have selected subtraction mode")
        op = MINUS
    elif x == "*":
        print("You have selected multiplication mode")
        op = MULTIPLY
    else:
        print("Invalid input")
        exit()
    start_game(mode, op) 

def intialize_player() : 
    username = input("Enter your username : ")
    print(f"Hello {username}! Welcome to the game")
    # how to check if a file exists in directory using python
    # I want to check if the file exists or not in ./stats directory by the name of username.txt
    # if it exists then I will read the file and display the stats of the player
    # if it does not exist then I will create a new file and write the stats of the player
    file_path = f"./stats/{username}.txt"
    if os.path.exists(file_path):
        print("You already exist in our database , enter password to proceed\n")

        tries=5
        while(tries > 0):
            password = input("Enter your password : ")
            pass_file = open("passwords.txt", "r")
            pass_lines = pass_file.readlines()
            if username + ' ' + password + "\n" in pass_lines : 
                print("Password correct")
                file = open(file_path, "r")
                print(file.read())
                file.close()
                break
            else:
                tries-=1
                print(f"Password incorrect, {tries} tries left")
        if (tries==0): exit()
    else:
        set_password(username)
        initialize_file(file_path)
    return file_path

os.system('clear')
file_path = intialize_player()

while(True):
    game(file_path)
    x = input("Do you want to play again? (yes/no) \n").strip().lower()
    if x == "no":
        break
    elif x == "yes":
        continue
    else:
        print("Invalid input")
        break