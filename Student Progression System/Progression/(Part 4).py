# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1999481
# Date: 10th April 2023
# Part 4

#User-defined function to calculate the progression outcome
def calculate_outcome(credits_pass,credits_defer,credits_fail):
    if credits_pass == 120:
        return "Progress"
    elif credits_pass == 100:
        return "Progress (module trailer)"
    elif credits_fail >= 80:
        return "Exclude"
    else:
        return "Do not progress - module Retriever"
    

#Main program 
#Predefined variables section
credits_range = [0, 20, 40, 60, 80, 100, 120]
progress = 0
trailer = 0
retriever = 0
exclude = 0
outcomes = 0
all_inputs = []
total_outcome = 0
dic = {}


while True:
    #Getting inputs
    std_id = input("\nEnter student ID : ")
    if not (std_id.startswith('w') and len(std_id) == 8 and std_id[1:].isnumeric()):
        print('Invalid Student ID\n')
        std_id = input("\nEnter student ID : ")

    #Making conditions 
    while True:
        try:
            credits_pass = int(input("\nEnter the pass credit: "))
            if credits_pass in credits_range:
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")

    while True:
        try:
            credits_defer = int(input("Enter the defer credit: "))
            if credits_defer in credits_range:
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")

    while True:
        try:
            credits_fail = int(input("Enter the fail credit: "))
            if credits_fail in credits_range:
                break
            else:
                print("Out of range")
                
        except ValueError:
            print("Integer required")

    #Total calculations
    if credits_pass + credits_defer + credits_fail == 120 :
        outcome = calculate_outcome(credits_pass,credits_defer,credits_fail)
        print(outcome)
        outcomes += 1
        
        if outcome == "Progress":
            progress += 1
            dic[std_id]='Progress - {},{},{}'.format(credits_pass,credits_defer,credits_fail)
        elif outcome == "Progress (module trailer)":
            trailer += 1
            dic[std_id]='Progress (module trailer) - {},{},{}'.format(credits_pass,credits_defer,credits_fail)
        elif outcome == "Do not progress - module Retriever":
            retriever += 1
            dic[std_id]='Do not progress - module Retriever - {},{},{}'.format(credits_pass,credits_defer,credits_fail)
        elif outcome == "Exclude":
            exclude += 1
            dic[std_id]='Exclude - {},{},{}'.format(credits_pass,credits_defer,credits_fail)

        all_inputs.append(outcome + ' - ' + str(credits_pass) + ", " + str(credits_defer) + ", " + str(credits_fail) + '\n')
    else:
        print("Total incorrect")

    #Repeat part
    print("\nWould you like to enter another set of data?")
    choice = input("Enter (y) to continue or (q) to quit: ")
    while choice != 'y' and choice != 'q':
        print("\nInvalid input. Please enter (y) or (q).")
        choice = input("\nEnter (y) to continue or (q) to quit: ")
    if choice == 'q':
        break

#Keys as k and values as v in the dictionary
print("-"*40)
for(k, v) in dic.items():                                                              
   print("{}:{}".format(k, v))
print("-"*40)
