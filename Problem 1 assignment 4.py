import random
def main():
    global Namelist
    Namelist = []
    get_winner(get_name())
    
def get_name():
    i = 0
    while True:
        name = input("Enter a name: ")
        if name == '':
            break
        else:
            Namelist.append(name)
    return (Namelist)
def get_winner(Namelist):
    try:
        winner = random.choice(Namelist)
        print (winner)
        Namelist.remove(winner)
        while True:
            choice = (input("choose another winner?: "))
            if choice == 'Y' or 'y':
                winner = random.choice(Namelist)
                print ("the winner is... ", winner)
                Namelist.remove(winner)
            else:
                print("The draw list is empty!")
                break
            
    except IndexError:
        print("The draw list is empty!")
main()


