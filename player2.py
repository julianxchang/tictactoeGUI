import socket
from gameboard import BoardClass

#Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#This function asks user for host information and creates the server
def createHost() -> object and str:
    """Creates a server on the ip/port spcified by the user.

    The function will ask the user to enter the ip and port of the server
    they want to set up. If server is valid, the function will create the server and
    begin listening for clients. The server will return a clientSocket object and 
    clientAddress string when a client successfully connects. If server is not valid,
    the function continuously ask the user until a valid server ip/port is entered.

    Args:
        None.

    Returns:
        clientSocket: clientSocket object that can then be used to send/recieve 
        data to/from the client.
        clientAddress: information on the client (ip/port)
    
    """
    while(True):
        try:
            ip = input("Input host ip address: ")
            port = int(input("Input host port number: "))
            serverSocket.bind((ip, port))
            serverSocket.listen(1)
            break
        except:
            print("Invalid server ip/port. Please try again.")
    print(f"Server is set up. Listening for clients on {ip}:{port}.")
    clientSocket, clientAddress = serverSocket.accept()
    return clientSocket, clientAddress
    

def move(player2) -> int and int:
    """Request input from user asking where they want to play their move.

    Args:
        None.

    Returns:
        row: row of the board.
        col: column of the board.
    """
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

def requestNames(clientSocket) -> str and str:
    """Gets client's username and server's username.

    This function will wait for the client to send their username. The server's
    username is automatically "player2" and the username will be sent to the client.

    Args:
        None.

    Returns:
        p1_name: client's username
        p2_name: server's username
    
    """
    p1_name = clientSocket.recv(1024).decode('ascii')
    p2_name = "player2"
    clientSocket.send(p2_name.encode())
    return p1_name, p2_name

def playAgain(clientSocket, p1_name) -> bool:
    """Waits for client response to see if the game should continue.

    Args:
        None.

    Returns:
        True: client want's to play again.
        False: client chose to end the game.
    
    """
    print(f"{p1_name} is choosing if they want to play again...")
    player1Choice = clientSocket.recv(1024).decode('ascii')
    if(player1Choice == "Play Again"):
        return True
    return False

def runGame(clientSocket, player2, p1_name, p2_name) -> None:
    """Runs the main game.

    Args:
        None.

    Returns:
        playAgain(): The function will call playAgain() when a winning
        move is detected.
    """
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

def runProgram():
    """Runs the entire program.

    Args:
        None.

    Returns:
        None.
    """
    clientSocket, clientAddress = createHost()
    print("Client connected from: ", clientAddress)
    print("Waiting for player1 username...")
    p1_name, p2_name = requestNames(clientSocket)
    player2 = BoardClass(p2_name, p2_name, 0, 0, 0, 0)
    cont = True
    while(cont):
        player2.resetGameBoard()
        player2.updateGamesPlayed()
        cont = runGame(clientSocket, player2, p1_name, p2_name)
    print(f"{p1_name} chose to end the game.")
    player2.printStats()
    serverSocket.close()

if __name__ == "__main__":
    runProgram()