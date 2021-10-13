string = "BANANA"
print(f'make a new word from {string} ')

user1= input(f" FARHAN IT'S YOUR TURN : ")
points= 0
if user1[0]==string[0] or user1[0]==string[2]:
    Farhan_Points= points +(string.count(user1))
    
    print(f' Farhan scored: {Farhan_Points} points' )


user2= input(f" FARAZ IT'S YOUR TURN : ")
vowels = "AEIOU"
points=0
if user2[0]== vowels[0]:
    Faraz_Points= points +(string.count(user2))
    print(f' Faraz scored: {Faraz_Points} points')

if Farhan_Points==Faraz_Points:
    print("draw")
elif Farhan_Points>Faraz_Points:
    print("Farhan won!")

else:
    print("Faraz won!")