import random
import string


choice1 = string.ascii_uppercase
choice2 = string.ascii_lowercase
choice3 = string.digits
choice4 = string.punctuation

choice=choice1 + choice2 + choice3 +choice3 + choice4

password=""
length=int(input("enter password length: "))

for value in range(length):
    password += random.choice(choice)

print("password is: ",password)






