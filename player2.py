import socket
from gameboard import BoardClass
import time

#Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This function asks user for host information and creates the server
def createHost() -> tuple:
    while(True):
        try:
            ip = input("Input host ip address: ")
            port = int(input("Input host port number: "))
            serverSocket.bind((ip, port))
            serverSocket.listen(5)
            break
        except:
            print("Invalid server ip/port. Please try again.")
    print("Server is set up. Listening for clients.")
    clientSocket, clientAddress = serverSocket.accept()
    return clientSocket, clientAddress
    

def move() -> None:
    possible_moves = "111213212223313233"
    while(True):
        choice = input("Please enter the row and column you want to choose (if you want top left, you would enter \"11\"): ")
        while(choice not in possible_moves or len(choice) != 2):
            print("Not a valid row/column.")
            choice = input("Please enter the row and column you want to choose (if you want top left, you would enter \"11\"): ")
        row = int(choice[0])-1
        col = int(choice[1])-1
        if(player2.isEmpty(row, col)):
            break
        else:
            print("Space is already taken. Please Try again.")
    return row, col

def requestNames() -> tuple:
    player1Name = clientSocket.recv(1024).decode('ascii')
    player2Name = "player2"
    clientSocket.send(player2Name.encode())
    return player1Name, player2Name

def playAgain() -> bool:
    print(f"{player1Name} is choosing if they want to play again...")
    player1Choice = clientSocket.recv(1024).decode('ascii')
    if(player1Choice == "Play Again"):
        return True
    return False

def runGame() -> None:
    print(f'Current Board (Opponent: {player1Name}):')
    player2.printBoard()
    while(True):
        print("Waiting for opponent to move.")
        player1Move = clientSocket.recv(1024).decode('ascii')
        player2.updateGameBoard(int(player1Move[0]), int(player1Move[1]))
        print(f'Current Board (Opponent: {player1Name}):')
        player2.printBoard()
        player2.setLastMove(player1Name)
        
        #Check if move by player1 was winning a move or was the last move
        if(player2.isWinner()):
            return playAgain()
        elif(player2.boardIsFull()):
            return playAgain()
        
        row, col = move()
        player2.updateGameBoard(row, col)
        clientSocket.send((str(row) + str(col)).encode())
        print(f'Current Board (Opponent: {player1Name}):')
        player2.printBoard()

        player2.setLastMove(player2Name)

        #Check if move by player2 was winning a move or was the last move
        if(player2.isWinner()):
            return playAgain()
        elif(player2.boardIsFull()):
            return playAgain()

if __name__ == "__main__":
    clientSocket, clientAddress = createHost()
    print("Client connected from: ", clientAddress)
    player1Name, player2Name = requestNames()
    player2 = BoardClass(player2Name, player2Name, 0, 0, 0, 0)
    cont = True
    while(cont):
        player2.resetGameBoard()
        player2.updateGamesPlayed()
        cont = runGame()
    print(f"{player1Name} chose to end the game.")
    player2.printStats()
    time.sleep(5)