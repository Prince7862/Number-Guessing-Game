import random;

chances = 0
randomNum = random.randint(1,9)

#print(randomNum)

#a = (randomNum > number)
#print(type(number))
#print(a)

while(chances < 5):

    chances = chances + 1
    
    number = int(input("Guess a Number from 1 to 9: "))

    if(number < randomNum):
        print("The number you have entered is less than the Random Number please retry")
        
    elif(number > randomNum):
        print("The number you have entered is more than the Random Number please retry")

    if(chances == 5):
        print("YOU LOSE!!! THE RANDOM NUMBER WAS: ",  randomNum)
        break

    elif(number == randomNum):
        print("CONGRATULATIONS YOU WIN!!!! ")
        break
