#LOOP
##############
#Initialization
##Set uo things that need to be done once and onlyonce
#Body
##Instruction that repeated
#Exit
##############
#For Loop
#1
#Write a program that displays on the screen the numbers from 1 to 100.
for count in range (1, 101):
    print (count)
#do it in while loop
count = 0
while count < 100:
    count += 1
    print(count)
#2
#Write a program that displays all the even numbers from 20 to 40.
for count in range (20, 41, 2):
    print(count)
#in while loop
count = 18
while count < 40:
    count += 2
    print(count)
#Write a program that displays all the odd numbers from 31 to 21
for count in range (31, 20, -2):
    print (count)
#while loop
count = 33
while count >21:
    count -= 2
    print(count)
# Write a program that asks the user to input two numbers.
# Your program should count from the first number to the second number. 
# Note that the first number is not always less than the second number.
running = True
while running == True:
    enterNum1 = input("number #1: ")
    enterNum2 = input("number #2: ")
    if enterNum1.isdigit() == True:
        enterNum1 = int(enterNum1)
        enterNum2 = int(enterNum2)
        if enterNum1 < enterNum2:
            num2 = enterNum2 + 1
            num1 = enterNum1
            for count in range(num1, num2):
                print(count)
        elif enterNum1 > enterNum2:
            num1 = enterNum1
            num2 = enterNum2 - 1
            for count in range (num1, num2, -1):
                print(count)
        else:
            print("please reenter the numbers.")
    elif enterNum1.isdigit() == False:
        if enterNum1 == str("quit"):
            running = False
        else:
            print("please reenter the numbers.")