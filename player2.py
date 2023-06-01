import socket
from gameboard import BoardClass

#This function asks user for host information and creates the server
def createHost(gui, ip, port) -> tuple[socket.socket, tuple[str, str], socket.socket]:
    #Create server socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((ip, port))
        gui.waitingText.set(f"Waiting for connection on {gui.connectionIP.get()}:{gui.connectionPort.get()}...")
        gui.hideConnectionScreen()
        gui.invalidServerLabel.grid_forget()
        gui.showWaitingForClientScreen()
        serverSocket.listen(1)
        clientSocket, clientAddress = serverSocket.accept()
        gui.waitingText.set("Player 1 connected! Waiting for them to input username...")
        requestNames(gui, clientSocket)
        return clientSocket
    except:
        gui.reloadConnectionScreen()
        gui.invalidServerLabel.grid(row=2,column=1)
        return False

def requestNames(gui, clientSocket) -> tuple[str, str]:
    p1Name = clientSocket.recv(1024).decode('ascii')
    gui.p1Name.set(p1Name)

def awaitClientMove(clientSocket, board):
    p1Move = clientSocket.recv(1024).decode('ascii')
    row, col = int(p1Move[0]), int(p1Move[1])
    board.updateGameBoard(row, col)
    return row, col

def move(clientSocket, board, row, col) -> tuple[int, int]:
    clientSocket.send((str(row) + str(col)).encode())
    board.updateGameBoard(row, col)

def awaitP1Choice(clientSocket, gui) -> bool:
    p1Choice = clientSocket.recv(1024).decode('ascii')
    gui.hideWaitingForClientScreen()
    if(p1Choice == "Play Again"):
        gui.restartGame()
    else:
        gui.showStatScreen()


if __name__ == "__main__":
    pass