import socket
from gameboard import BoardClass
from tictactoeGUI import tictactoeGUI

def connect_to_host(gui, ip, port):
    #Create connection socket object
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connectionSocket.connect((ip,port))
        gui.destroyConnectionScreen()
        gui.showRequestNameScreen()
        return connectionSocket
    except:
        gui.showErrorClientScreen()

def requestNames(connectionSocket, p1Name) -> tuple[str, str]:
    if(not p1Name.isalnum()):
        raise ValueError
    else:
        connectionSocket.send(p1Name.encode())

def moveClient(connectionSocket, board, row, col) -> tuple[int, int]:
        connectionSocket.send((str(row) + str(col)).encode())

def playAgain(connectionSocket) -> bool:
    choice = input("Would you like to play another game (y/n): ").lower()
    while(choice != 'y' and choice != 'n'):
        print("Invalid input.")
        choice = input("Would you like to play another game (y/n): ").lower()
    if choice == 'y':
        connectionSocket.send(b'Play Again')
        return True
    else:
        connectionSocket.send(b'Fun Times')
        return False

def runGame(player1, p1_name, p2_name, connectionSocket) -> bool:
    print(f'Current Board (Opponent: {p2_name}):')
    player1.printBoard()
    while(True):
        player1.updateGameBoard(row, col)
        connectionSocket.send((str(row) + str(col)).encode())
        print(f'Current Board (Opponent: {p2_name}):')
        player1.printBoard()

        player1.setLastMove(p1_name)

        # Check if move by player1 was a winning move or was the last possible move
        if(player1.isWinner()):
            return playAgain(connectionSocket)
        elif(player1.boardIsFull()):
            return playAgain(connectionSocket)

        # Receive move from server
        print("Waiting for opponent to move...")
        player2Move = connectionSocket.recv(1024).decode('ascii')
        player1.updateGameBoard(int(player2Move[0]), int(player2Move[1]))
        print(f'Current Board (Opponent: {p2_name}):')
        player1.printBoard()

        player1.setLastMove(p2_name)

        # Check if move from server was a winning move or was the last possible move
        if(player1.isWinner()):
            return playAgain(connectionSocket)
        elif(player1.boardIsFull()):
            return playAgain(connectionSocket)

def runProgram() -> None:
    tictactoeGUI("Client")
    '''
    startgame, connectionSocket = gui.getStartGame(), 90
    if(startgame):
        p1_name, p2_name = requestNames(connectionSocket)
        player1 = BoardClass(p1_name, p2_name, 0, 0, 0, 0)
        cont = True
        while(cont):
            player1.resetGameBoard()
            player1.updateTotalGames()
            cont = runGame(player1, p1_name, p2_name, connectionSocket)
        player1.printStats()
    connectionSocket.close()
    '''
if __name__ == "__main__":
    runProgram()
