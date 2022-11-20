import random
import string
# The main function contains the lists used for the program, it also calls the function password_gen.
# The length, special, and numpref ask the user for input and because those are called in the password_gen
# function the information is then passed to that function.
def main():
    global chars, spec_char, num
    chars = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    spec_char = ['!','@','#','$','%','&']
    num = ['0','1','2,','3','4','5','6','7','8','9']

    length = int(input("what's the minimum length? "))
    special = int(input("How many special characters? "))
    numpref = int(input("How many numbers? ")) 

    password_gen(length, special, numpref)

def password_gen(length, special, numpref):
    password_list = []
    password = ""
    temp = []

    # Calculates how many 'normal' characters there are. 
    char_total = int(length - special - numpref)

    # Populates temporary list with characters based on user input
    temp += (random.sample(chars, char_total))
    temp += (random.sample(spec_char, special))
    temp += (random.sample(num, numpref))

    # shuffles temporary list to generate 3 passwords, appends each to a list of passwords
    for i in range(3):
        random.shuffle(temp)
        password = ''.join(temp)
        password_list.append(password)

    print("you can choose below password ", password_list)

    # choice-1 to account for indices starting at 0
    choice = int(input("which one you prefer? "))-1
    try:
        print("you choose password", password_list[choice])
    except IndexError:
        print("choice out of the range")

main()