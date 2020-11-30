# Boris Paul Pizha  
# Simple Game Project 


print("Rock Paper Scissors game in Python")


from random import randint

def round(items):
  
   # Reading player 1 input
   player = input("Please enter your choice Rock, Paper, Scissors: ")
  
   # Generating random number between 1, 100
   compChance = randint(1,100)
          
   # Deciding computer choice
   if compChance < 33:
       computerChoice = 1
   elif compChance >= 33 and compChance <= 66:
       computerChoice = 2
   else:
       computerChoice = 3
      
   computer = items[computerChoice-1]
  
   # Computer
   #  input
   print("\n Computer chose: " + items[computerChoice-1]  + ". \n" )
  
   # Storing player inputs in list
   inputs = [player.upper(), computer.upper()]
  
   return inputs
  

def main():
  
   options_to_choose = ["Rock", "Paper", "Scissors"]
  
   inputs = round(options_to_choose)
  
   while inputs[0] == inputs[1]:
       inputs = round(options_to_choose)
  
   if inputs == ['ROCK', 'PAPER'] or inputs == ['PAPER', 'ROCK']:
       if inputs[0] == 'PAPER':
           print("\n You win, because Paper covers Rock \n")
       else:
           print("\n You lose, because Paper covers Rock \n")
          
   
   elif inputs == ['ROCK', 'SCISSORS'] or inputs == ['SCISSORS', 'ROCK']:

       if inputs[0] == 'ROCK':

           print("\n You win, because Rock smashes scissors\n")
       else:
           print("\n You lose, because Rock smashes scissors \n")


   elif inputs == ['SCISSORS', 'PAPER'] or inputs == ['PAPER', 'SCISSORS']:
       if inputs[0] == 'SCISSORS':

           print("\n You win, because Scissors cut paper \n")
       else:
           print("\n You lose,becasue Scissors cut paper \n")
  
    
        
   else:
       print("\n Invalid Error Please Try Again \n")

    
      
      
# Calling main function
main()