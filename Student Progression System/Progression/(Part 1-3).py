# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1999481
# Date: 27th March 2023
# Part 1 , Part 2 , Part 3

#user-defined function to calculate the progression outcome
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
credits_range = [0,20,40,60,80,100,120]
progress = 0
trailer = 0
retriever = 0
exclude = 0
outcomes = 0
all_inputs = []
total_outcome = 0


Results = open("Results.txt","w")

while True:
    
    #Getting inputs
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

    #Total calculation
    if credits_pass + credits_defer + credits_fail == 120:
        outcome = calculate_outcome(credits_pass,credits_defer,credits_fail)
        print(outcome)
        outcomes += 1
        
        #Making decisions
        if outcome == "Progress":
            progress += 1
        elif outcome == "Progress (module trailer)":
            trailer += 1
        elif outcome == "Do not progress - module Retriever":
            retriever += 1
        elif outcome == "Exclude":
            exclude += 1

        all_inputs.append(outcome + ' - ' + str(credits_pass) + ", " + str(credits_defer) + ", " + str(credits_fail) + '\n')
    else:
        print("Total incorrect")
        
    #Repeat part
    print("\nWould you like to enter another set of data?")         
    choice = input("Enter (y) to continue or (q) to quit: ")
    while choice != 'y' and choice != 'q':
        print("Invalid input. Please enter (y) or (q).")
        choice = input("Enter (y) to continue or (q) to quit: ")
    if choice == 'q':
        break
    
print("-"*40)

#Histogram
print("\nHistogram")
print(f"Progress\t: {progress * '*'} ")
print(f"Trailer\t\t: {trailer * '*'} ")
print(f"Retriever\t: {retriever * '*'} ")
print(f"Exclude\t\t: {exclude * '*'} ")
print("-" *40)
print(str(outcomes) + "  outcomes in total")
print("-" *40)

print("-" *40)

#Enter data to list
for i in range(len(all_inputs)):
    print(all_inputs[i])

print("-"*40)

#Making text file
with open("Results.txt", "w") as inputs:
    inputs.writelines(all_inputs)
    
#Display data in the text file
print ("\nData in the text file:\n")
Results = open('Results.txt','r')
content = Results.read()
print (content)
Results.close
