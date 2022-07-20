#Objective is to simulate a magic 8 ball with 20 different outcomes that randomly assign to a question asked by the user, and then provides a randomly generates a fortune
#Decided to add my own twist and make it have some pretty fun answers instead of a standard magic 8 ball

import random
import time

print('███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░  ░█████╗░  ██████╗░░█████╗░██╗░░░░░██╗░░░░░')
print('████╗░████║██╔══██╗██╔════╝░██║██╔══██╗  ██╔══██╗  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░')
print('██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝  ╚█████╔╝  ██████╦╝███████║██║░░░░░██║░░░░░')
print('██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗  ██╔══██╗  ██╔══██╗██╔══██║██║░░░░░██║░░░░░')
print('██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝  ╚█████╔╝  ██████╦╝██║░░██║███████╗███████╗')
print('╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░  ░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝')
print('⢠⢤⠁⠤⢼⠀⠤⡄⢠⠠⠇⡤⢼⠀⡤⡕⢠⠤⡀⢠⢀⠀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⢠⢀⠀⡡⡄⠀⠠⡄⠠⢤⠀⡤⠼⢠⠤⡅⢠⢠⠀⡥⢄⠠⡤⡅⢠⠄')
print('⢸⣉⣖⣎⣹⣒⣉⣑⣺⣉⣖⣏⣹⣲⣉⣷⣺⣉⣗⣮⠽⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠯⣱⣲⣉⣗⣊⣉⣒⣏⣱⣺⣉⣗⣎⣉⣒⣏⣹⣲⣉⣗⣺⡁')
print('⢼⠼⡤⡬⢼⠤⠧⠧⢼⠬⡤⡧⢼⢤⠧⢧⣼⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⠴⠶⠦⠤⣄⡀⠀⠀⠙⠻⣷⣼⠼⠤⡧⢥⢼⠥⡧⡼⠼⠤⡧⢿⢤⠧⡧⢼⠼')
print('⢸⣲⡃⢓⣺⠘⣒⡎⢸⣒⠃⣗⣺⠘⣦⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡾⠚⠁⠀⠀⠀⣀⣀⡀⠀⠈⠑⠦⣀⠀⠈⠑⢽⣏⣗⡊⢸⣒⡏⢳⣲⠉⣗⣺⠘⣖⡏⢹⡢')
print('⢽⢠⠯⢧⢼⠭⡄⡬⢽⢠⠯⡧⣼⣿⣿⠃⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⡟⠁⠀⠀⢠⣶⣿⠿⠿⣿⣷⡄⠀⠀⠉⢷⡄⠀⠀⠹⣷⡼⢽⠤⡯⢧⢠⠭⡇⣸⠽⡄⡯⢽⢀')
print('⢸⠚⣖⡞⢺⣲⠓⢓⣺⠚⣖⣳⣿⣿⡇⠀⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⣿⣿⣇⢀⣀⣾⣿⣧⣤⡀⠀⠀⢳⡀⠀⠀⠈⢻⣾⠓⣗⡚⠚⣒⡗⢻⣲⠓⣗⣺⠊')
print('⢸⠽⣅⡩⢽⣀⠭⢇⣸⠭⣰⢟⣿⣿⡇⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠙⠿⢿⣿⡿⠋⠉⠙⣿⣿⡄⠀⠸⡇⠀⠀⠀⠈⣿⡭⡇⡸⢽⣀⡯⢽⣀⠯⣇⣸⠝')
print('⢺⢲⠓⠓⢺⠒⡆⡖⢺⢲⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢸⣿⣷⣀⣀⣠⣿⣿⠃⠀⢠⣟⠀⠀⠀⠀⣿⣿⡓⢳⢲⠓⡗⣾⠚⡖⡗⢺⢰')
print('⢸⣉⡯⢏⢹⠽⡉⡩⢍⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠈⠻⢿⣿⡿⠿⠛⠁⠀⠀⣼⣿⣧⠀⠀⢀⣿⠋⣧⢏⢩⠭⣏⣹⠽⡉⡯⢽⢁')
print('⢸⠚⡆⡔⢺⠠⠒⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣆⣠⣾⣿⠀⢿⡜⠚⠄⡗⢺⢠⠓⡧⢸⠊')
print('⢸⠹⡉⡩⢹⣉⡇⣏⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣈⡹⢹⣉⡏⢽⢉⡏⣏⣹⠰')
print('⢸⢠⠃⠣⢸⠒⠆⡖⢺⡏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢸⢷⢰⠒⡇⢼⠘⡄⡗⢺⢠')
print('⢸⣉⡇⢏⢹⢈⡉⡉⢸⣇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⣾⢏⢩⠅⣏⣹⠸⡉⡇⢸⢁')
print('⢸⠚⡆⡔⢺⢀⠖⠇⢸⢻⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⡯⠜⠺⠄⡗⢺⢠⠓⡇⣸⠊')
print('⢸⠰⣇⣩⢸⣈⡅⣏⣹⠈⣧⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣾⣇⣹⢸⣉⡇⢼⣈⡇⣏⣹⠰')
print('⢸⢠⠇⠣⢸⠐⠆⡖⢺⠠⠛⣧⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣼⠧⡇⢣⢰⠒⡇⢼⠘⡄⡗⢺⢠')
print('⢸⣉⣏⣏⣸⣹⣁⡉⣹⣈⣏⣟⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢡⣾⣻⣉⡏⣏⣙⣏⣏⣹⣹⣁⣏⣽⣀')
print('⢸⠐⡤⡔⢸⠤⠆⠣⢼⠐⡤⡗⢺⢫⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣵⡟⢣⢼⠐⡧⡼⠸⠤⡇⢺⢤⠃⡧⢼⠘')
print('⣸⣰⣋⣑⣺⣉⣇⣏⣹⣚⣉⣗⣺⣉⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣾⣋⣗⣋⣹⣂⣏⣹⣺⣉⣇⣺⣉⣖⣏⣹⣰')
print('⢸⢤⠇⠧⢼⠲⠤⡤⢺⠤⠇⡧⢼⠸⡤⡷⢹⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠯⢤⠔⡧⠼⢺⠤⡇⢧⢤⠂⡧⢼⠸⡤⡗⢾⢄')
print('⢺⡉⣗⡎⣹⣒⣉⣑⣺⢉⣖⡏⣹⣲⡋⣷⣺⣉⡿⠝⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣻⡉⣗⣊⣉⣒⡋⣱⣺⢉⣗⣎⢉⣒⡏⢹⣲⣉⣗⣺⠉')
print('⢸⠼⡤⡬⢼⠤⠧⠧⢼⠬⡤⡯⢼⢤⠧⣧⢌⠁⠀⠀⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠀⢀⠽⡧⠼⠼⠤⡧⢥⢼⠥⡧⡼⠼⡤⡧⢽⢤⠧⡧⢼⠜')
print('⢸⢲⠃⠓⢺⠈⡒⡎⢺⠒⠃⡗⢺⠘⡖⠎⢹⠒⡏⢲⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⡖⡎⠙⠒⡇⠑⢲⠁⡗⠊⢸⠒⡏⢳⢲⠉⡗⢺⠈⡖⡏⢹⠂')
print('')
print('')
print('')
print('Hello Stranger, I am the mysterious Magic 8 Ball, What is your name?')
#define input for name 
name = input()
print('')
print('Welcome to the Magic 8 Ball, ' + name)
print('')
count_str = input("How many questions would you like to ask the almighty and most powerful 8-Ball? --> ")
print('')

#Provides feedback to user entered digit, which also includes what happens if they answer with a non numerical answer,
#or, enters in a number that the 8 ball feels is excessive
while True:
    if count_str.isdigit():
        count = int(count_str)
        break
    else:
        count_str = input("Uh...That is not a number? Try Again: ")
print('')
if count <= 0:
    print("Well, some one isn't a team player!")
    time.sleep(5)
    exit()
elif count > 10:
    print("I feel like you shouldn't be consulting a Magic 8 Ball for this many questions...Let's just do one and go from there :)", sep='')
    count = 1
    

#Sequence options for random choices as randomly chosen by function below.
answers = ["It is certain that it will happen.", "Looks like a Yes!", "Without a doubt, yes.", "Absolutely", "1000% Yes.",
           "My sources tell me this is definite.", "It could happen, chances are it will.", "I'm really not sure, possibly?", "Yes.", "Maybe", "Ask again, I wasn't paying attention",
           "Sorry, I just woke up, what was your question?", "It's not looking too good.", "ERROR", "Prediction unclear. Try again if you dare.",
           "I wouldn't put money on it.", "Absolutely not", "No. Nope. No Chance.", "Not this time", "Very doubtful."]

#Here is the main loop, which generates answer with slight delay. which includes an exit function and prompt once the determined number of questions has been answered.
while count > 0:
    blah = input("Type your Yes/No Question here --> ")
    dice = random.choice(answers)
    

#Delay output for 1 second each to simulate a "computing" effect.
    print("Thinking about this...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print()
    print("\n", dice, "\n", sep='')
    time.sleep(2)
#counts down the amount of questions in order to have program conclude
    count = count - 1


#Here is the exit prompt after stated number of questions have been answered, and it closes the program.
else:
    print("I hope this helped! If not, tough luck...")
    time.sleep(2)
    print("██╗████████╗  ██╗░░██╗░█████╗░░██████╗  ░██████╗██████╗░░█████╗░██╗░░██╗███████╗███╗░░██╗")
    print("██║╚══██╔══╝  ██║░░██║██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░██║")
    print("██║░░░██║░░░  ███████║███████║╚█████╗░  ╚█████╗░██████╔╝██║░░██║█████═╝░█████╗░░██╔██╗██║")
    print("██║░░░██║░░░  ██╔══██║██╔══██║░╚═══██╗  ░╚═══██╗██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚████║")
    print("██║░░░██║░░░  ██║░░██║██║░░██║██████╔╝  ██████╔╝██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║")
    print("╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝")
    time.sleep(3)
    exit()
