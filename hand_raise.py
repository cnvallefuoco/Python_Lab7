import random

def name():
    #first_name1 = input("Please enter your first name: ").capitalize()
    first_name1 = "Carina"
    #last_name1 = input ("Please enter your last name: ").capitalize()
    last_name1 = "Vallefuoco"
    initial = last_name1[0]
    team_member1 = first_name1+initial
    print(team_member1)
    #first_name2 = input("Please enter your first name: ").capitalize()
    first_name2 = "Marc"
    #last_name2 = input ("Please enter your Last name: ").capitalize()
    last_name2 = "Acevedo"
    initial = last_name2[0]
    team_member2 = first_name2+initial
    print(team_member2)

list = []

def readFile(fileName):
    while True:
        try:
            fileName = open(input('Enter the name of the file that you wish to read from:\n'), 'r')
        except IOError:
            print('Not a valid file destination')
        else:
            break



def menu():

    for line in readfile:
    print(line[:-1])
    list.append(line)

    print('\nThe following students are in this class:\n',list, '\n', sep="")

    random.choice(list)

    reselect = input('\nWould you like to randomly select a student? Yes or No:\n').lower()

    name_attempt = random.choice(list)

    while name_attempt != "CarinaV" or name_attempt != "MarcA":
        print (name_attempt)
        reselect = input('\nWould you like to randomly select a student? Yes or No:\n').lower()
        if reselect == 'yes':
            # print (name_attempt)
            # reselect = input('\nWould you like to randomly select a student? Yes or No:\n').lower()
            name_attempt = random.choice(list)
        else:
            break

def main():

    menu()

main()
