import random
#########################################
# Random password generator
#########################################

# Generate random password with
# uppercase letters, lowercase letters,
# and numbers.
def get_password():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    capitals = characters.upper()
    numbers = '0123456789'
    special = '$#!&'
    output = ''

    for i in range(16):
        choice = random.randint(0,3)
        if(choice == 0):
            output += characters[random.randint(0,25)]
        elif(choice == 1):
            output += capitals[random.randint(0,25)]
        elif(choice == 2):
            output += numbers[random.randint(0,9)]
        elif(choice == 3):
            output += special[random.randint(0,3)]
        else:
            print("Something blew up")
    return output

