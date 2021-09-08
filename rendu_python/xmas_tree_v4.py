# This program prints the brand new christmas tree with some christmas balls.

'''
Generating top branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars).
'''


def top_branches():

    nb_spaces = 15
    stars_top = 1
    nb_branches = 4

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 1
        stars_top += 2


'''
Generating middle branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars). 
'''


def mid_branches():

    nb_spaces = 12
    stars_top = 7
    nb_branches = 3

    print(" " * 12, "0", "*" * 3, "0")

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 2
        stars_top += 4


'''
Generating bottom branches module, input = number of blank space, number of starting "stars" (top of the module),
number of branches (row of stars). 
'''


def bot_branches():

    nb_spaces = 10
    stars_top = 11
    nb_branches = 3

    print(" " * 8, "0", " " * 3 + "*" * 5, " " * 2, "0")

    for i in range(nb_branches):
        print(" " * nb_spaces, "*" * stars_top)
        nb_spaces -= 3
        stars_top += 6


'''
Generating garlands, input = number of blank space, height of the trunk (row of stars) and number of star for the trunk.
'''


def garlands():

    nb_spaces = 5
    trunk_height = 1
    stars_top = 5

    for i in range(trunk_height):
        print(" " * nb_spaces, "| " * 4 + "*" * stars_top + " |" * 4)

    for i in range(trunk_height):
        print(" " * nb_spaces, "0 " * 4 + "*" * stars_top + " 0" * 4)


'''
Generating trunk shape, input = number of blank space, number of starting "stars" (top of the module),
height of the trunk (row of stars). 
'''


def trunk_shape():

    nb_spaces = 13
    stars_top = 5
    trunk_height = 1

    for i in range(trunk_height):
        print(" " * nb_spaces, "*" * stars_top)


'''
function that call the other functions
'''


def main():
    top_branches()
    mid_branches()
    bot_branches()
    garlands()
    trunk_shape()


main()
