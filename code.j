#The array for the spaces on the board    
box = [" "," ", " ", " ", " ", " ", " ", " "," " ]

#This function displays the board
def board():
    print(1,"|",2,"|",3)
    print("--+---+--")
    print(4,"|",5,"|",6)
    print("--+---+--")
    print(7,"|",8,"|",9)   
    print(" ")
    print(" ")

#Function to print the board
def print_board():
    print(box[0],"|",box[1],"|",box[2])
    print("--+---+--")
    print(box[3],"|",box[4],"|",box[5])
    print("--+---+--")
    print(box[6],"|",box[7],"|",box[8])

#Asks player what position they want to place marker
def position_of_piece(num,mark):
    position = int(input("%s,insert the space you want to place the %s: "%(num,mark)))
    position = position - 1

    return position

#This is where the game starts
def main():
    #Prints board to give instructions to the player on the numbers for the positions
    board()
    #This call for the function 'print_board' to display the board
    print_board()

    #This loop controls the number of goes each player has
    for i in range(9):
        if i%2==0:
            player = "Player 1"
            marker = "X"
        else:
            player = "Player 2"
            marker ="O"

        #The players choices for which position they choose are stored in variable position
        position = position_of_piece(player,marker)

        if box[position] == " ":
            box[position] = marker
            print_board()
        else:
            print("Position is already taken, chose a different position.")
            position = position_of_piece(player,marker)
            box[position] = marker
            print_board()
        
        

        

main()
