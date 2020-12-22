#Ruchi Mukerjee
#00250518
#CIS153-O1A 
#Final Project

#Greet the user
print('Hello there! Welcome to the Resident Evil Resistance tool for players.')
#input to start different parts
answer=input('Would you like to view global statistics, estimate RP, or enter your own win/loss record? Type global, estimate, or record to continue.')

#SECTION 1
#Prints image of either mastermind or survivor
#then prints either mastermind or survivor dictionary with their win rates
if answer == 'global':
    stats=input('Do you want to view survivor or mastermind statisitcs? Please type survivor or mastermind. ')
    if stats == 'mastermind':
        #importing image of a mastermind
        import socket
        import time
#host name defines the website we want to pull data from, as written in our textbook
        HOST = 'residentevil.net'
        #port 80 is the http port
        PORT = 80
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((HOST, PORT))
        mysock.sendall(b'GET http://www.residentevil.net/resistance/pc/img/common/mastermind/kB6q4A7Z.jpg HTTP/1.0\r\n\r\n')
        count = 0
        picture = b""

        while True:
            data = mysock.recv(5120)
            if len(data) < 1: break
         #time.sleep(0.25)
            count = count + len(data)
            print(len(data), count)
            picture = picture + data
        mysock.close()

        pos = picture.find(b"\r\n\r\n")
        print('Header length', pos)
        print(picture[:pos].decode())

        picture = picture[pos+4:]
        fhand = open("kB6q4A7Z.jpg", "wb")
        fhand.write(picture)
        fhand.close()
#dictionary for mastermind win rates
        mcounts = { 'nicholai' : 73.3 , 'spencer' : 75.6, 'annette' : 75.6, 'alex' : 77.5, 'daniel' : 77.5}
        lst = list(mcounts.keys())
        #sorts in alphabetical order
        lst.sort()
        print(lst)
        print('Mastermind win rates are in percentages, updated as of 12/21/20.')
        for key in lst:
            #prints mastermind win rates
            print(key, mcounts[key])
#elif statement if user inputs survivor
    elif stats == 'survivor':
        #imports different image of a survivor than of a mastermind as written above
        import socket
        import time

        HOST = 'residentevil.net'
        PORT = 80
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((HOST, PORT))
        mysock.sendall(b'GET http://www.residentevil.net/resistance/pc/img/common/survivor/rH7WFimY.jpg HTTP/1.0\r\n\r\n')
        count = 0
        picture = b""

        while True:
            data = mysock.recv(5120)
            if len(data) < 1: break
            #time.sleep(0.25)
            count = count + len(data)
            print(len(data), count)
            picture = picture + data
            
        mysock.close()
        
        pos = picture.find(b"\r\n\r\n")
        print('Header length', pos)
        print(picture[:pos].decode())

        picture = picture[pos+4:]
        fhand = open("rH7WFimY.jpg", "wb")
        fhand.write(picture)
        fhand.close()
    #survivor win rates is saved in a dictionary called scounts
        scounts = { 'valerie' : 23.7 , 'becca' : 21.4, 'jill': 20.6 , 'samuel' : 21, 'january' : 23.1, 'tyrone' : 22.6, 'martin' : 22.6}
        lst = list(scounts.keys())
        #sorts in alphabetical order
        lst.sort()
        print(lst)
        print('Survivor win rates are in percentages. Updated as of 12/21/20.')
        for key in lst:
            #prints survivor win rates
            print(key, scounts[key])
    
    else: 
        print('Your answer was invalid. The program will close now.')
#SECTION 2
#result points estimation
#nested if statements are used to print the correct result point range
elif answer == 'estimate':
    print('This will ask a series of questions that will give you a possible range for match scores/result points.')
    #estimate1 is the first variable to determine result points
    #defining variable
    estimate1=input('Did you win or lose the match?')
    #if statement for estimate 1
    if estimate1 == 'win':
        print('Next question')
        #creaturecount is the next variable
        creaturecount=input('Did you kill many creatures, or few/none? Enter either many or few.')
        #next if statement for creaturecounts, this one is nested under the first for estimate1
        if creaturecount == 'few':
            print('Next question')
            #defining variable
            objectives=input('Did you complete any of the objectives yourself? Enter correct or incorrect.')
            #next if statement for objectives, nested under the creaturecounts
            if objectives == 'incorrect':
                #enough variables have been evaluated and a estimate is printed.
                print('Your estimated result point range if you did not completely any objectives yourself is 2500-3000.')
            #elif statement is for when the user inputs the other answer rather than incorrect
            elif objectives == 'correct':
                #enough variables have been evaluated and a estimate is printed.
                print('Your estimated result point range is 2700-3200.')
        #elif statement for when the user answers the other answer with the creaturecount variable
        elif creaturecount == 'many':
            #objectives variable is used again for the user's input to define it in this scenario
            objectives=input('Did you complete any of the objectives yourself? Enter correct or incorrect.')   
            #new if statement for this defined objectives, nested under the creaturecounts if statement
            if objectives == 'incorrect':
                print('Your estimated result point range if you did completely any objectives by yourself is 3000-3999.')
            #if other answer was used in objectives, this elif statement is run
            elif objectives == 'correct':
                print('Your estimated result point range is 4000-5000.')
   #if user inputs they have lost the following nested if statements are used, elif for a different response from the first question
    elif estimate1 == 'lose':
        #area is a different variable needed when someone has lost
        area=input('Did you lose in area 1, 2, or 3? Please enter only the number.')
        #area has been defined as a variable above. The following nested if statements are based on other factors.
        if area == '1':
            #another result is printed, area 1 loss doesn't have a lot of factors
            print('Your estimated result point range is 1-1500.')
        #elif for next answer in if statement with area as variable
        elif area == '2':
            #area 2 has a unique element, area2loss variable was created
            area2loss=input('Did you get the security card? Type yes or no.')   
            #next if statement nested under area if statement
            if area2loss == 'yes':
                #another factor depended on area2loss is number of terminals completed
                terminal=input('How many terminals did you complete? Type 1, 2, or 3.')
                #next if statement nested under areatwoloss variable
                if terminal == '1':
                    print('Your estimated result point range is 1500-2000')
                #elif if answer is 2
                elif terminal == '2':
                    print('Your estimated result point range is 1700-2400')
                #elif if answer is 3
                elif terminal == '3':
                    print('Your estimated result point range is 2000-2700.')
            #if the area2loss was no
            elif area2loss == 'no':
                print('Your estimated result point range is 1000-1700.')
        #if the first question in this section was area 3, these next lines come into play
        elif area == '3':
            #core is the last variable needed to determine result points
            core=input('How many cores did you destroy? Type none, 1, 2, or 3')
            #if statement nested under area if statement
            if core == 'none':
                print('Your estimated result point range is 2100-3200')
            #elif statements if answer is other options
            elif core == '1':
                print('Your estimated result point range is 2700-3500')
            elif core == '2':
                print('Your estimated result point range is 3000-3900')
            elif core == '3':
                print('Your estimated result point range is 4000-5000. Using an RP booster can bring the score even above 5000.')
    #if the user typed somthing other than win or lose from the the first question in this section, this is printed
    else:
        print('Your answer was invalid. The program will close now.')
    
#SECTION 3
#calculating user record
#a dictionary with all 12 characters is created. User inputs their own record that is stored in the dictionary
elif answer == 'record':
    print('This section will prompt you for your wins and losses.')
    #dictionary created, called character counts with all 12 characters
    charactercounts = { 'nicholai' : 0 , 'spencer' : 0, 'annette' : 0, 'alex' : 0, 'daniel' : 0, 'valerie' : 0, 'becca' : 0, 'jill': 0, 'samuel' : 0, 'january' : 0, 'tyrone' : 0, 'martin' : 0}
    while True:
#while loop to continue asking for win and loss rate and character entry until done        
        print( charactercounts )
        n = input('Enter name or q to quit')
        #if the name user entered is in dictionary as a key, then user is prompted for win and loss numbers, calculate win rate, winrate is assigned to name in dictionary
        if n in charactercounts:
            wins = int(input('Enter wins'))
            loss = int(input('Enter losses'))
            if loss == 0:
                winrate=100
            else:
            #converts user inputyed wins and losses into a win rate percentage
                winrate = (wins / loss)*100
            charactercounts[n] = winrate
        #closes this section of the program, leading to the last line asking to press enter to exit
        elif n == 'q':
            break
        #if someone types in something other than a name in the dictionary
        else:
            print('not an option')
#users inputs are entered into the dictionary and the dictionary is printed
    print( charactercounts )

#if user typed in a wrong answer to the first question the program asked, this is printed.  
else:
    print('Your answer was invalid. The program will close now.')
    
#End with this statement to make Python show the evaluation
input('Press Enter to exit')

