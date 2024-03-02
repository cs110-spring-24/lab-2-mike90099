import random
num = random.randint(1, 100)

user = input("Enter your guess: ")
user = int(user)

#loop for whole guess
 
while user > num:
    print("Too high, it was", num)
    print("Too high!")
    print("Guess a number between...",)
    print((num),"and",())
if user > num:
    print("Too high!")
    print("Guess a number between...",)
    print((num),"and",(num+50))
count = 0
while count < 500:
    count =count + 1
    if count % 4 == 0:
        continue
    else:
        print(count)