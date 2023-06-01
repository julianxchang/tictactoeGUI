import socket
from gameboard import BoardClass
from tictactoeGUI import tictactoeGUI

#This function asks user for host information and creates the server
def createHost(gui, ip, port) -> tuple[socket.socket, tuple[str, str], socket.socket]:
    #Create server socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((ip, port))
        gui.waitingText.set(f"Waiting for connection on {gui.connectionIP.get()}:{gui.connectionPort.get()}...")
        gui.destroyConnectionScreen()
        gui.label3.destroy()
        gui.showWaitingForClientScreen()
        serverSocket.listen(1)
        clientSocket, clientAddress = serverSocket.accept()
        gui.waitingText.set("Player 1 connected! Waiting for them to input username...")
        requestNames(gui, clientSocket)
        return clientSocket
    except:
        gui.reloadConnectionScreen()
        gui.showErrorServerScreen()

def requestNames(gui, clientSocket) -> tuple[str, str]:
    print("waiting for p1 username")
    p1Name = clientSocket.recv(1024).decode('ascii')
    gui.p1Name.set(p1Name)

def moveServer(player2) -> tuple[int, int]:
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

def playAgain(clientSocket, p1_name) -> bool:
    print(f"{p1_name} is choosing if they want to play again...")
    player1Choice = clientSocket.recv(1024).decode('ascii')
    if(player1Choice == "Play Again"):
        return True
    return False

def runGame(player2, p1_name, p2_name, clientSocket) -> bool:
    print(f'Current Board (Opponent: {p1_name}):')
    player2.printBoard()
    while(True):
        # Receive move from client
        print("Waiting for opponent to move...")
        player1Move = clientSocket.recv(1024).decode('ascii')
        player2.updateGameBoard(int(player1Move[0]), int(player1Move[1]))
        print(f'Current Board (Opponent: {p1_name}):')
        player2.printBoard()

        player2.setLastMove(p1_name)

        #Check if move from client was winning a move or was the last possible move
        if(player2.isWinner()):
            return playAgain(clientSocket, p1_name)
        elif(player2.boardIsFull()):
            return playAgain(clientSocket, p1_name)

        # Request input from user and send move to server
        row, col = move(player2)
        player2.updateGameBoard(row, col)
        clientSocket.send((str(row) + str(col)).encode())
        print(f'Current Board (Opponent: {p1_name}):')
        player2.printBoard()

        player2.setLastMove(p2_name)

        #Check if move by player2 was a winning move or was the last possible move
        if(player2.isWinner()):
            return playAgain(clientSocket, p1_name)
        elif(player2.boardIsFull()):
            return playAgain(clientSocket, p1_name)

def runProgram() -> None:
    tictactoeGUI("Server")
    '''
    clientSocket, clientAddress, serverSocket = createHost()
    print("Client connected from: ", clientAddress)
    print("Waiting for player1 username...")
    p1_name, p2_name = requestNames(clientSocket)
    player2 = BoardClass(p2_name, p2_name, 0, 0, 0, 0)
    cont = True
    while(cont):
        player2.resetGameBoard()
        player2.updateTotalGames()
        cont = runGame(player2, p1_name, p2_name, clientSocket)
    print(f"{p1_name} chose to end the game.")
    player2.printStats()
    serverSocket.close()
    '''
if __name__ == "__main__":
    runProgram()