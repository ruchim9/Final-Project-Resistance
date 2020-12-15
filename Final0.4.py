#Ruchi Mukerjee
#00250518
#CIS153-O1A 
#Final Project

#Greet the user
print('Hello there! Welcome to the Resident Evil Resistance tool for players, currently in progress.')
#input to start different parts
answer=input('Would you like to view global statistics, estimate RP, or enter your own win/loss record? Type global, estimate, or record to continue.')
#this answer reads the website and prints the statistics. If I can't get it to read the statistics I will make it print the most current statistics from the official website
    if answer == 'global'
    #review ch 12
    
    elif answer == 'estimate'
        print('This will ask a series of questions that will give you a possible range for match scores.')
        estimate1=input('Did you win or lose the match?')
            if estimate1 == 'win'
                creaturecount=input('Did you kill many creatures, or few/none? Enter either many or few.')
                objectives=input('Did you complete any of the objectives yourself? Enter yes or no.')
                    #if statement that factors both of these variables in?
                else:
                        print('Your answer was invalid. The program will close now.')
            elif estimate1 == 'lose'
                area=input('Did you lose in area 1, 2, or 3? Please enter only the number.')
                    if area == '1'
                    elif area == '2'
                    elif area == '3'
                    else:
                        print('Your answer was invalid. The program will close now.')
            else:
                print('Your answer was invalid. The program will close now.')
    elif answer == 'record'
    
    else:
    print('Your answer was invalid. The program will close now.')
    
#End with this statement to make Python show the evaluation
    input('Press Enter to exit')
