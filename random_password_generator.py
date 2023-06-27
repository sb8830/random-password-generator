import secrets 
import string
import random

def main():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    allChars = lower + upper + digits + special 
    password = ""

    pwlen = int(input("Password Size: "))
    no_of_password = int(input("Password requirements: "))
    minUpper = int(input("Minimum Upper Case: "))
    minLower = int(input("Minimum Lower Case:"))
    minDigits = int(input("Minimum Numbers:"))
    minSpec = int(input("Minimum Special: "))

    allChars2 = minUpper + minLower + minDigits + minSpec

    for i in range(minUpper):
        password += "".join(random.choice(secrets.choice(upper)))

    for i in range(minLower):
        password += "".join(random.choice(secrets.choice(lower)))

    for i in range(minDigits):
        password += "".join(random.choice(secrets.choice(digits)))

    for i in range(minSpec):
        password += "".join(random.choice(secrets.choice(special)))

    remaining = pwlen - minUpper - minLower - minDigits - minSpec


    for i in range(remaining):
        password += "".join(random.choice(secrets.choice(allChars)))

   
    password = list(password)
    random.shuffle(password)
    if(allChars2 <= pwlen):
        for i in range(no_of_password):
            random.shuffle(password)
            print("".join(password))
    else:
        print("Invalid")

    main()
main()