import socket
from gameboard import BoardClass

def connect_to_host(gui, ip, port) -> socket.socket:
    """Connects to server on the ip/port specified by the user.

    The function will take in the ip and port as parameters and if server information
    is valid, the function will connect to the server.
    If the sever information passed in is invalid, an exception will be raised and the function
    will call the method showErrorClientMessageBox() in the clientGUI class.

    Args:
        gui: clientGUI object used to directly modify the GUI.
        ip (str): server ip address.
        port (str): server port.

    Returns:
        connectionSocket: socket object that can then be used to send/receive
        data to/from the server.
    """
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connectionSocket.connect((ip, int(port)))
        gui.destroyConnectionScreen()
        gui.showRequestNameScreen()
        return connectionSocket
    except:
        gui.showErrorClientMessageBox()

def requestNames(connectionSocket, gui, p1Name) -> str:
    """Sends the client username to server through socket and waits for server
    to send their username.

    Args:
        connectionSocket: socket object used to send client's username to server.
        gui: clientGUI object used to directly modify the GUI.
        p1Name: client's username.

    Returns:
        p2Name: server's username

    Raises:
        ValueError: Raises valueerror if username entered is not alphanumeric.
    """
    if(not p1Name.isalnum()):
        raise ValueError
    else:
        connectionSocket.send(p1Name.encode())
        gui.showWaitingForServerScreen()
        p2Name = connectionSocket.recv(1024).decode('ascii')
        return p2Name

def move(connectionSocket, board, row, col) -> None:
    """Sends the move made by client to server and updates gameboard.

    Args:
        connectionSocket: socket object used to send move.
        board: BoardClass object used to get information about the board.
        row: row of client's move.
        col: column of client's move.

    Returns:
        None.
    """
    connectionSocket.send((str(row) + str(col)).encode())
    board.updateGameBoard(row, col)

def awaitServerMove(connectionSocket, board) -> tuple[int, int]:
    """Receives the move made by server.

    Args:
        connectionSocket: socket object used to receive server's move.
        board: BoardClass object used to get information about the board.

    Returns:
        row: row of server's move.
        col: column of server's move.
    """
    p2Move = connectionSocket.recv(1024).decode('ascii')
    row, col = int(p2Move[0]), int(p2Move[1])
    board.updateGameBoard(row, col)
    return row, col

def playAgain(connectionSocket, gui) -> None:
    """Function is called when client decides to play again. This function will call
    the method restartGame() in clientGUI class.

    Args:
        connectionSocket: socket object used send client's choice.
        gui: clientGUI object used to directly modify the GUI.

    Returns:
        None.
    """
    connectionSocket.send(b"Play Again")
    gui.restartGame()

def endGame(connectionSocket, gui) -> None:
    """Function is called when client decides to end game. This function will call
    the methods in clientGUI class to show the final stats screen.

    Args:
        connectionSocket: socket object used send client's choice.
        gui: clientGUI object used to directly modify the GUI.

    Returns:
        None.
    """
    connectionSocket.send(b"Fun Times")
    gui.destroyMainGame()
    gui.showStatScreen()

def runGame() -> None:
    """Runs the entire game by creating the clientGUI object.

    Args:
        None.

    Returns:
        None.
    """
    import clientGUI
    clientGUI.clientGUI()

if __name__ == "__main__":
    runGame()
