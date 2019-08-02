#################################################################################################
#Samael Newgate
#4/14/2018
#CSC102
#################################################################################################
#Rules of the game (and the program):
#
#Player and “house” start with a score of 0 before the first roll.  Scores for both are accumulated through the number of rolls (1,2, and 3). 
#For each roll of the 2 dice: NOTE – this does not require a loop as we have not covered this, but you may use loops if you have moved ahead and mastered them.
#If the sum of the dice is 7 or 11, display “CRAPS” and increment “house score by 2”.
#If the dice are the same value (doubles) and the values are even, increment the player score by 2 (NOTE – you should use the modulo operator with an operand of 2 for determining whether the value is even). 
#If the dice are the same value (doubles) and the values are odd, increment the “house” score by 2.  
#If not CRAPS or doubles, and the total is less than 7, houseScore = houseScore +2.
#If not CRAPS or doubles, and the total is greater than 7, playerScore = playerScore + 2.
#Determine the winner and display the results (with 3 rolls, there cannot be a tie!).
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.

from random import randint #imports random generator 
print ("------------------------------------------------------")
print ('Welcome Player!\nFeeling lucky today?\nLets find out!')
print ('------------------------------------------------------')

#Variables

Player = 0 #sets player score to 0                 
house = 0  #sets house score to 0 
Craps1 = False #sets craps variable to false 
Craps2 = False #sets craps variable to false
Craps3 = False #sets craps variable to false
Double1 = False #sets double variable to false 
Double2 = False #sets double variable to false 
Double3 = False #sets double ariable to false 
Dice1 = randint(1,6) #dice used in Alpha 
Dice2 = randint(1,6) #dice used in Alpha
Dice3 = randint(1,6) #dice used in Beta
Dice4 = randint(1,6) #dice used in Beta
Dice5 = randint(1,6) #dice used in Gamma
Dice6 = randint(1,6) #dice used in Gamma
Roll_1_total = Dice1 + Dice2  ##
Roll_2_total = Dice3 + Dice4   ## Totals 
Roll_3_total = Dice5 + Dice6  ##

def Aplha(): #Roll 1
                         ##
    global Player         #                     
    global house          #
    global Dice1          # References global 
    global Dice2          #     Variables
    global Craps1         #
    global Double1        #
    global Roll_1_total  ##
    
    print ('Rolling the dice') # rolling the dice for the first time 
    print ('Rolled a',Dice1,'and',Dice2) #display what was rolled 
    print (Roll_1_total) #displays total 
    if Roll_1_total == 7 or Roll_1_total == 10: #rules for getting Craps 
        print ('Craps!')
        Craps1 = True #marks when rolled Craps
        house += 2
    if (Dice1 == 2 and Dice2 == 2): #Rules for even double's
        Double1 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 2')
    if (Dice1 == 4 and Dice2 == 4): #Rules for even double's
        Double1 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 4')
    if (Dice1 == 6 and Dice2 == 6): #Rules for even double's
        Double1 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 6')
    if (Dice1 == 1 and Dice2 == 1): #Rules for odd double's 
        Double1 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 1')
    if (Dice1 == 3 and Dice2 == 3): #Rules for odd double's
        Double1 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 3')
    if (Dice1 == 5 and Dice2 == 5): #Rules for odd double's
        Double1 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 5')
    if (Roll_1_total < 7 and Double1 == False and Craps1 == False): #rules for no Craps or doubles and roll total is greater than 7 
        print ('I win this round')
        house += 2 #increses house score by 2
    if (Roll_1_total > 7 and Double1 == False and Craps1 == False): #rules for no Craps or doubles and roll total is less than 7 
        print ('You win this round')
        Player += 2 #increses house score by 2
        

# call the function        
Aplha()

def Beta(): #Roll 2
                         ##
    global Player         #
    global house          #
    global Dice3          # Referances Global 
    global Dice4          #     Variables
    global Craps2         #
    global Double2        #
    global Roll_2_total  ##
    
    print ('Rolling the dice again') #rolling the dice for a second time 
    print ('Rolled a',Dice3,'and',Dice4) #displays what was rolled 
    print (Roll_2_total) #displays total 
    if Roll_2_total == 7 or Roll_2_total == 10: #rules for getting Craps
       print ('CRAPS!') 
       Craps2 = True #marks when rolled Craps
       house += 2
    if (Dice3 == 2 and Dice4 == 2): #Rules for even double's
        Double2 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 2')
    if (Dice3 == 4 and Dice4 == 4): #Rules for even double's
        Double2 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 4')
    if (Dice3 == 6 and Dice4 == 6): #Rules for even double's
        Double2 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 2')
    if (Dice3 == 1 and Dice4 == 1): #Rules for odd double's
        Double2 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 1')
    if (Dice3 == 3 and Dice4 == 3): #Rules for odd double's
        Double2 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 3')
    if (Dice3 == 5 and Dice4 == 5): #Rules for odd double's
        Double2 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 5')
    if (Roll_2_total < 7 and Double2 == False and Craps2 == False): #rules for no Craps or doubles and roll total is greater than 7 
        print ('I win this round')
        house += 2 #increses house score by 2
    if (Roll_2_total > 7 and Double2 == False and Craps2 == False): #rules for no Craps or doubles and roll total is less than 7
        Player += 2 #increses players score by 2
  

# call the function       
Beta()

def Gamma(): #Roll 3 
                         ##
    global Player         #
    global house          #
    global Dice5          # Referances Global 
    global Dice6          #     Variables 
    global Craps3         #
    global Double3        #
    global Roll_3_total  ##
    
    print ('Rolling the dice one more time') #rolling the dice for a third time 
    print ('Rolled a',Dice5,'and',Dice6) #displays what was rolled 
    print (Roll_3_total) #displays total 
    if Roll_3_total == 7 or Roll_3_total == 10: #rules for getting Craps
        print ('CRAPS!') 
        Craps3 = True #marks when rolled Craps
        house += 2
    if (Dice5 == 2 and Dice6 == 2): #Rules for even double's
        Double3 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 2')
    if (Dice5 == 4 and Dice6 == 4): #Rules for even double's
        Double3 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 4')
    if (Dice5 == 6 and Dice6 == 6): #Rules for even double's
        Double3 = True #marks when rolled even doubles
        Player += 2 #increses players score by 2
        print ('Doubles of 6')
    if (Dice5 == 1 and Dice6 == 1): #Rules for odd double's
        Double3 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 1')
    if (Dice5 == 3 and Dice6 == 3): #Rules for odd double's
        Double3 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 3')
    if (Dice5 == 5 and Dice6 == 5): #Rules for odd double's
        Double3 = True #marks when rolled odd doubles
        house += 2 #increses house score by 2
        print ('Doubles of 5')
    if (Roll_3_total < 7 and Double3 == False and Craps3 == False): #rules for no Craps or doubles and roll total is greater than 7 
        print ('I win this round')
        house += 2 #increses house score by 2
    if (Roll_3_total > 7 and Double3 == False and Craps3 == False): #rules for no Craps or doubles and roll total is less than 7
        print ('You win this round')
        Player += 2 #increses players score by 2
        

#call the function        
Gamma()

print ('------------------------------------------------------')

print ('House score is:',house) #shows house score total 
print ('Player score is:',Player)#shows players total score 
if (house > Player): #conditions for the house to win 
    print ('I Win the game\nBetter luck next time.')
if (house < Player): #conditions for the player to win 
    print ('You won the game!\nCongratulations!!')
