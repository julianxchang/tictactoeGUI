import socket
from gameboard import BoardClass
import time

#Create connection socket
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This fucntion will ask user for host information and attempt to connect
def connectToHost() -> bool:
    while True:
        try:
            ip = input("Enter host ip address: ")
            port = int(input("Enter host port number: "))
            connectionSocket.connect((ip,port))
            return True
        except:
            valid_input = "YyNn"
            choice = input("Connection could not be made. Would you like to try again (y/n): ")
            while(choice not in valid_input):
                print("Invalid input.")
                choice = input("Connection could not be made. Would you like to try again (y/n): ")
            if choice == "n" or choice == "N":
                return False

def move() -> tuple:
    possible_moves = "111213212223313233"
    while(True):
        choice = input("Please enter the row and column you want to choose (if you want top left, you would enter \"11\"): ")
        while(choice not in possible_moves or len(choice) != 2):
            print("Not a valid row/column.")
            choice = input("Please enter the row and column you want to choose (if you want top left, you would enter \"11\"): ")
        row = int(choice[0])-1
        col = int(choice[1])-1
        if(player1.isEmpty(row, col)):
            break
        else:
            print("Space is already taken. Please Try again.")
    return row, col

def requestNames() -> tuple:
    player1Name = input("Please enter your username: ")
    while(not player1Name.isalnum()):
        print("Please only enter alphanumeric usernames.")
        player1Name = input("Please enter your username: ")
    player1Name = (player1Name.encode())
    connectionSocket.send(player1Name)
    player1Name = player1Name.decode('ascii')
    player2Name = connectionSocket.recv(1024).decode('ascii')
    return player1Name, player2Name
    
def playAgain() -> bool:
    valid_choice = "YyNn"
    choice = input("Would you like to play another game (y/n): ")
    while(choice not in valid_choice):
        print("Invalid input.")
        choice = input("Would you like to play another game (y/n): ")
    if choice == 'y' or choice == 'Y':
        connectionSocket.send(b'Play Again')
        return True
    else:
        connectionSocket.send(b'Fun Times')
        return False

def runGame() -> None:
    print(f'Current Board (Opponent: {player2Name}):')
    player1.printBoard()
    while(True):
        row, col = move()
        player1.updateGameBoard(row, col)
        connectionSocket.send((str(row) + str(col)).encode())
        print(f'Current Board (Opponent: {player2Name}):')
        player1.printBoard()

        player1.setLastMove(player1Name)

        #Check if move by player1 was winning a move or was the last move
        if(player1.isWinner()):
            return playAgain()
        elif(player1.boardIsFull()):
            return playAgain()
        
        print("Waiting for oppoent to move...")
        player2Move = connectionSocket.recv(1024).decode('ascii')
        player1.updateGameBoard(int(player2Move[0]), int(player2Move[1]))
        print(f'Current Board (Opponent: {player2Name}):')
        player1.printBoard()

        player1.setLastMove(player2Name)

        #Check if move by player2 was winning a move or was the last move
        if(player1.isWinner()):
            return playAgain()
        elif(player1.boardIsFull()):
            return playAgain()



if __name__ == "__main__":
    startGame = connectToHost()
    if(startGame):
        player1Name, player2Name = requestNames()
        player1 = BoardClass(player1Name, player2Name, 0, 0, 0, 0)
        cont = True
        while(cont):
            player1.resetGameBoard()
            player1.updateGamesPlayed()
            cont = runGame()
        player1.printStats()
        time.sleep(5)