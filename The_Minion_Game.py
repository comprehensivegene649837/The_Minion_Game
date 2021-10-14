print('''*****HELLO! WELCOME TO THe MINION GAME*****
 \nFollow the given instructions to play it: 

There is a string named "BANANA" and then the users/players have to input a bunch of words or a single word to make a new word from the string and then that word will be checked for how many times it occurs in the string. 
Say for instance, player 1 inputs "BAN" and "BAN" appears just once in the string so they will be given 1 point and it's a double player game so the same process will be taken out by player 2 or will be applied to player 2.

note:
#1 ( player one has to input a word or bunch of words starting from a consonant)
#2 (player 2 to has to input a word or bunch of words starting from a vowel)
#3 All the words or bunch of words should be in capital letters
#4 Don't repeat the words!
#5 To exit the game, kindly type "end"
''' )

import random
import re #regular expression
string = ["BANANA" , "APPLE", "MANGO"]
string2= random.choice(string)

input("press enter if you have read the instruction: ")
print(f'make as many words as you can from the word {string2} ')

user1points= 0
while True:
    user1= input(f" USER1 IT'S YOUR TURN : ")
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    
    if user1 == 'end':
        break
   
    if user1 in string2 and user1[0].lower() in consonants:
        user1points= user1points + (string2.count(user1))   #len(re.findall(f'(?={user1})', string))
    
    else:
        print("sorry! type in capital letters and first letter should be a consonant")

print(f' USER1 scored: {user1points} points' )

user2points= 0
while True:
    user2= input(f" USER2 IT'S YOUR TURN : ")
    vowels = [ 'a', 'e', 'i', 'o', 'u']

    if user2 == 'end':
        break
   
    if user2 in string2 and user2[0].lower() in vowels:
        user2points= user2points + len(re.findall(f'(?={user2})', string2))
    else:
        print("sorry! type in capital letters and and first letter should be a vowel")
print(f' USER2 scored: {user2points} points' )

if user1points==user2points:
    print("draw")
elif user1points>user2points:
    print("User1 won!")
else:
    print("User2 won!")
