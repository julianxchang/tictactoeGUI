import socket
from gameboard import BoardClass

#This function asks user for host information and creates the server
def createHost(gui, ip, port) -> tuple[socket.socket, tuple[str, str], socket.socket]:
    #Create server socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((ip, port))
        gui.master.resizable(1,1)
        gui.master.geometry("280x100")
        gui.master.resizable(0,0)
        gui.waitingText.set(f"Waiting for connection on:\n{gui.connectionIP.get()}:{gui.connectionPort.get()}")
        gui.hideConnectionScreen()
        gui.hideErrorServerScreen()
        gui.showWaitingForClientScreen()
        serverSocket.listen(1)
        clientSocket, clientAddress = serverSocket.accept()
        gui.master.resizable(1,1)
        gui.master.geometry("370x100")
        gui.master.resizable(0,0)
        gui.waitingText.set("Client connected!\nWaiting for them to input username...")
        requestNames(gui, clientSocket)
        return clientSocket
    except:
        gui.showErrorServerScreen()
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