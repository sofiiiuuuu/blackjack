#Defined values for all string cards
A=1
Q=10 
J=10 
K=10 
#here I define borrow as yes, that way everytime the player puts 
#yes in borrow it can execute the borrow program
borrow = "yes"
#here i import random to shuffle the cards
import random
#here I use tuple to degine the deck as all cards multiplied by 4 to
#have the full deck
all_cards=[A,2,3,4,5,6,7,8,9,J,Q,K,11] * 4
random.shuffle(all_cards)
#this selects the first two cards
card1 = all_cards.pop()
card2 = all_cards.pop()
#this sums the points
sum_of_points = card1 + card2
#this prints the sum and the card names or values
print(sum_of_points, card1, card2) 
print("You got:", card1, card2) 

#in case the winner didnt get 21 the first round this will say if they
#lost or can borrow
if sum_of_points > 21: 
    print("Sorry, you lost!")
elif sum_of_points == 21: 
    print("Congratulations! You won!") 
#here it asks if you want to borrow, you should answer in yes
else: 
    borrow = input("Would you like to borrow a card? ")
#this prints the card names
print("Total:", sum_of_points) 

#everytime the player puts yes, or Yes it will give them a 
# new card (this is why i use .lower(), otherwise it will only
#take into accout the "yes" not "Yes")
#and add it to the points, then it analyses if they won or not
#if they have less than 21 you can borrow again
while borrow.lower() == "yes":
    new_card = all_cards.pop()
    sum_of_points += new_card
    print("You got:", new_card) 
    print("Total:", sum_of_points) 
    if sum_of_points > 21: 
        print("Sorry, you lost!")
        #this breaks the loop
        break
    elif sum_of_points == 21: 
        print("Congratulations! You won!") 
        break
    else: 
        borrow = input("Would you like to borrow a card? ")
    
    
    