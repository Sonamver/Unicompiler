import random
Name = input("Enter name:")
print("Enter the range that you want to give:")
begin, end = map(int , input().split('-'))

a = random.randint(begin, end)

count = 0
score = 50

while (score!=0):
    b = int(input("Guess the number:"))
    if a == b:
        print(f"You guessed the correct no. in {count} guesses.")
        print(f"you got {score} points.")
        break
    else:
        score = score - 5
        count = count+1
        print ("hint")
        if a > b:
            print("Try greater than that number.")
        else:
            print("Try smaller number than that.")
        if(a%2==0):
            print("Try even number")
        else:
            print("Try odd number")
