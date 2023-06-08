import socket
from gameboard import BoardClass

#This function asks user for host information and creates the server
def createHost(gui, ip, port) -> socket.socket or False:
    """Creates a server on the ip/port specified by the user.

    The function will take in the ip and port as parameters and if server information
    is valid, the function will create the server and begin listening for clients.
    Once a client connects, the function will call requestP1Name and return the socket object.
    If the sever information passed in is invalid, an exception will be raised and the function
    will call the method showErrorServerMessageBox() in the serverGUI class.

    Args:
        gui: serverGUI object used to directly modify the GUI.
        ip (str): server ip address.
        port (str): server port.

    Returns:
        clientSocket: socket object that can then be used to send/receive
        data to/from the client.
    """
    #Create server socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serverSocket.bind((ip, int(port)))
        gui.showSuccessfulServerScreen()
        serverSocket.listen(1)
        clientSocket, clientAddress = serverSocket.accept()
        gui.showClientConnectedScreen()
        requestP1Name(gui, clientSocket)
        return clientSocket
    except:
        gui.showErrorServerMessageBox()

def requestP1Name(gui, clientSocket) -> None:
    """Receives the username sent by the client.

    Args:
        gui: serverGUI object used to directly modify the GUI.
        clientSocket: socket object used to receive client's username.

    Returns:
        None.
    """
    p1Name = clientSocket.recv(1024).decode('ascii')
    gui.p1Name.set(p1Name)
    gui.destroyWaitingForClientScreen()
    gui.showRequestNameScreen()

def sendP2Name(clientSocket, p1Name, p2Name) -> None:
    """Sends the server username to client.

    Args:
        clientSocket: socket object used to send servers username to client.
        p1Name: client's username.
        p2Name: server's username.

    Returns:
        None.
    """
    from serverGUI import invalidUsername, dupUsername
    if(not p2Name.isalnum()):
        raise invalidUsername
    elif(p2Name == p1Name):
        raise dupUsername
    else:
        clientSocket.send(p2Name.encode())

def awaitClientMove(clientSocket, board) -> tuple[int, int]:
    """Receives the move made by client.

    Args:
        clientSocket: socket object used to receive client's move.
        board: BoardClass object used to get information about the board.

    Returns:
        row: row of client's move.
        col: column of client's move.
    """
    p1Move = clientSocket.recv(1024).decode('ascii')
    row, col = int(p1Move[0]), int(p1Move[1])
    board.updateGameBoard(row, col)
    return row, col

def move(clientSocket, board, row, col) -> None:
    """Sends the move made by server to client and updates gameboard.

    Args:
        clientSocket: socket object used to send move.
        board: BoardClass object used to get information about the board.
        row: row of server's move.
        col: column of server's move.

    Returns:
        None.
    """
    clientSocket.send((str(row) + str(col)).encode())
    board.updateGameBoard(row, col)

def awaitP1Choice(clientSocket, gui) -> None:
    """Receives client's choice of whether or not they want to play again.

    Args:
        clientSocket: socket object used to receive client's username.
        gui: serverGUI object used to directly modify the GUI.

    Returns:
        None.
    """
    p1Choice = clientSocket.recv(1024).decode('ascii')
    if("Play Again" in p1Choice and len(p1Choice)>10):
        gui.restartGame(p1Choice[10:])
    elif(p1Choice == "Play Again"):
        gui.restartGame("none")
    else:
        gui.destroyMainGame()
        gui.showStatScreen()

def runGame() -> None:
    """Runs the entire game by creating the serverGUI object.

    Args:
        None.

    Returns:
        None.
    """
    import serverGUI
    serverGUI.serverGUI()

if __name__ == "__main__":
    runGame()