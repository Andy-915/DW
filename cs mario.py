def main():
    print_square(2)

def print_square(size):

    #For each row in square
    for i in range(size):

        #For each brick in row
        for j in range(size):

            #Print brick
            print("#", end="")
        #To get a new line only at the end of the row not the end of every brick
        print()

main()
