import socket
from gameboard import BoardClass

def connect_to_host(gui, ip, port):
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connectionSocket.connect((ip,port))
        gui.hideConnectionScreen()
        gui.showRequestNameScreen()
        return connectionSocket
    except:
        gui.showErrorClientScreen()

def requestNames(connectionSocket, p1Name) -> tuple[str, str]:
    if(not p1Name.isalnum()):
        raise ValueError
    else:
        connectionSocket.send(p1Name.encode())

def move(connectionSocket, board, row, col) -> tuple[int, int]:
        connectionSocket.send((str(row) + str(col)).encode())
        board.updateGameBoard(row, col)

def awaitServerMove(connectionSocket, board):
    p2Move = connectionSocket.recv(1024).decode('ascii')
    row, col = int(p2Move[0]), int(p2Move[1])
    board.updateGameBoard(row, col)
    return row, col

def playAgain(connectionSocket, gui):
    connectionSocket.send(b"Play Again")
    gui.restartGame()

def endGame(connectionSocket, gui):
    connectionSocket.send(b"Fun Times")
    gui.showStatScreen()

if __name__ == "__main__":
    pass
