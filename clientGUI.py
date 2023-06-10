import tkinter as tk
from tkinter import messagebox
from threading import Thread
from player1 import *
from gameboard import BoardClass

class clientGUI():
    """A class to create the client tictactoe GUI object.

    Attributes:
        socket (Socket object): socket object used to send and receive messages.
        board (BoardClass object): BoardClass object used to get information about
        the current board.
        font (tuple): tuple containing font information for the GUI.
    """
    def __init__(self) -> None:
        """Creates a clientGUI and sets up the Tkinter canvas and initiates the
        Tkinter variables. Also calls methods that creates the widgets. Finally,
        it will call the method that starts mainloop.

        Args:
            None.

        Returns:
            None.
        """
        self.socket = object
        self.board = object
        self.font = ('Small Fonts', 13)
        self.canvasSetup()
        self.initTKVariables()
        self.createConnectionScreen()
        self.createRequestNameScreen()
        self.createWaitingForServerScreen()
        self.createStatScreen()
        self.showConnectionScreen()
        self.runUI()

    def initTKVariables(self) -> None:
        """Initiates the Tkinter variables.

        Args:
            None.

        Returns:
            None.
        """
        self.connectionIP = tk.StringVar()
        self.connectionIP.set('localhost')
        self.connectionPort = tk.StringVar()
        self.connectionPort.set('8000')
        self.p1Name = tk.StringVar()
        self.p2Name = tk.StringVar()
        self.currentTurn = tk.StringVar()
        self.endLabelText = tk.StringVar()
        self.p1NameStat = tk.StringVar()
        self.p2NameStat = tk.StringVar()
        self.gamesPlayedStat = tk.StringVar()
        self.winStat = tk.StringVar()
        self.lossStat = tk.StringVar()
        self.tieStat = tk.StringVar()

    def canvasSetup(self) -> None:
        """Sets up the Tkinter canvas.

        Args:
            None.

        Returns:
            None.
        """
        self.master = tk.Tk()
        self.master.title('Client')
        self.master.geometry('526x570')
        self.master.resizable(1,1)

    def createConnectionScreen(self) -> None:
        """Creates the connection screen widgets.

        Args:
            None.

        Returns:
            None.
        """
        self.connectionIPLabel = tk.Label(self.master, text='Host Name (or IP address)', font=self.font)
        self.connectionIPEntry = tk.Entry(self.master, textvariable=self.connectionIP, font=self.font, width=25)
        self.connectionPortLabel = tk.Label(self.master, text='Port', font=self.font)
        self.connectionPortEntry = tk.Entry(self.master, textvariable=self.connectionPort, font=self.font, width=15)
        self.colonLabel = tk.Label(self.master, text=':', font=self.font)
        self.connectionInputButton = tk.Button(self.master, text='Connect', font=self.font, command=Thread(target=lambda:self.attemptConnection(self.connectionIP.get(), self.connectionPort.get())).start, height=2)

    def createRequestNameScreen(self) -> None:
        """Creates the request name screen widgets.

        Args:
            None.

        Returns:
            None.
        """
        self.requestNameLabel = tk.Label(self.master, text='Please enter your username (only alphanumeric):', font=self.font)
        self.requestNameInput = tk.Entry(self.master, textvariable=self.p1Name, font=self.font)
        self.usernameButton = tk.Button(self.master, text='Send Username', command=Thread(target=lambda:self.confirmUsername(self.p1Name.get())).start, font=self.font, height=2)
        self.invalidNameLabel = tk.Label(self.master, text='Username can only be alphanumeric. Please try again.', fg='red', font=self.font)

    def createWaitingForServerScreen(self) -> None:
        """Creates the waiting for server screen widget.

        Args:
            None.

        Returns:
            None.
        """
        self.waitingForServerLabel = tk.Label(self.master, text="Waiting for server to input username...", font=self.font)

    def createMainGame(self) -> None:
        """Creates the widgets for the main game.

        Args:
            None.

        Returns:
            None.
        """
        self.playerLabel = tk.Label(self.master, text=f"Your Name: {self.p1Name.get()}", font=self.font)
        self.currentTurnLabel = tk.Label(self.master, textvariable=self.currentTurn, font=("Small Fonts", 15))
        self.opponentLabel = tk.Label(self.master, text=f"Opponent Name: {self.p2Name.get()}", font=self.font)
        self.btn1 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn1)).start, height=2, width=5)
        self.btn2 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn2)).start, height=2, width=5)
        self.btn3 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn3)).start, height=2, width=5)
        self.btn4 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn4)).start, height=2, width=5)
        self.btn5 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn5)).start, height=2, width=5)
        self.btn6 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn6)).start, height=2, width=5)
        self.btn7 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn7)).start, height=2, width=5)
        self.btn8 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn8)).start, height=2, width=5)
        self.btn9 = tk.Button(self.master, text=' ', font=('Small Fonts', 40), command=Thread(target=lambda:self.btnClick(self.btn9)).start, height=2, width=5)

    def createStatScreen(self) -> None:
        """Creates the widgets for the stats screen.

        Args:
            None.

        Returns:
            None.
        """
        self.statsTitleLabel = tk.Label(self.master, text='Final Stats', font=self.font, fg='red')
        self.p1NameLabel = tk.Label(self.master, textvariable=self.p1NameStat, font=self.font, width=40)
        self.p2NameLabel = tk.Label(self.master, textvariable=self.p2NameStat, font=self.font)
        self.gamesPlayedLabel = tk.Label(self.master, textvariable=self.gamesPlayedStat, font=self.font)
        self.winLabel = tk.Label(self.master, textvariable=self.winStat, font=self.font)
        self.lossLabel = tk.Label(self.master, textvariable=self.lossStat, font=self.font)
        self.tieLabel = tk.Label(self.master, textvariable=self.tieStat, font=self.font)

    def showConnectionScreen(self) -> None:
        """Uses .grid() to place the widgets to display connection screen.

        Args:
            None.

        Returns:
            None.
        """
        self.connectionInputButton['state'] = 'normal'
        self.master.geometry('459x152')
        self.master.resizable(0,0)
        self.connectionIPLabel.grid(row=0, column=0, padx=(20,0), pady=(20,0), sticky='W')
        self.connectionIPEntry.grid(row=1, column=0, padx=(20,0))
        self.connectionPortLabel.grid(row=0, column=2, pady=(20,0), sticky='W')
        self.connectionPortEntry.grid(row=1, column=2)
        self.colonLabel.grid(row=1, column=1)
        self.connectionInputButton.grid(row=2, columnspan=3, padx=(20,0), pady=5, sticky='news')

    def showErrorClientMessageBox(self) -> None:
        """Shows a error message box if the client is unable to connect to the server.
        If user clicks "yes", the connection screen will be regenerated and if the user
        clicks "no", the program will terminate.

        Args:
            None.

        Returns:
            None.
        """
        cont = tk.messagebox.askquestion('Connection Error', 'Connection could not be made. Try again?')
        if(cont == 'yes'):
            self.destroyConnectionScreen()
            self.createConnectionScreen()
            self.showConnectionScreen()
        else:
            self.master.quit()

    def showRequestNameScreen(self) -> None:
        """Uses .grid() to place the widgets to display request name screen.

        Args:
            None.

        Returns:
            None.
        """
        self.master.resizable(1,1)
        self.master.geometry('387x158')
        self.master.resizable(0,0)
        self.requestNameLabel.grid(row=0, column=0, padx=20, pady=(20,0))
        self.requestNameInput.grid(row=1, padx=20, pady=(0,5), sticky='news')
        self.usernameButton.grid(row=2, padx=20, sticky='news')

    def showWaitingForServerScreen(self) -> None:
        """Uses .grid() to place the widgets to display waiting for server screen.

        Args:
            None.

        Returns:
            None.
        """
        self.master.resizable(1,1)
        self.master.geometry('325x75')
        self.master.resizable(0,0)
        self.destroyRequestNameScreen()
        self.waitingForServerLabel.grid(padx=20, pady=20)

    def showMainGame(self) -> None:
        """Uses .grid() to place the widgets to display main game screen.

        Args:
            None.

        Returns:
            None.
        """
        self.master.resizable(1,1)
        self.master.geometry('522x590')
        self.master.resizable(0,0)
        self.playerLabel.grid(row=0, column=0, columnspan=2, padx=(10,0), sticky='W')
        self.opponentLabel.grid(row=0, column=1, columnspan=2, sticky='E')
        self.btn1.grid(row=1, column=0, padx=(10,5), pady=5)
        self.btn2.grid(row=1, column=1, padx=5, pady=5)
        self.btn3.grid(row=1, column=2, padx=5, pady=5)
        self.btn4.grid(row=2, column=0, padx=(10,5), pady=5)
        self.btn5.grid(row=2, column=1, padx=5, pady=5)
        self.btn6.grid(row=2, column=2, padx=5, pady=5)
        self.btn7.grid(row=3, column=0, padx=(10,5), pady=5)
        self.btn8.grid(row=3, column=1, padx=5, pady=5)
        self.btn9.grid(row=3, column=2, padx=5, pady=5)
        self.currentTurnLabel.grid(row=4, columnspan=3)

    def showStatScreen(self) -> None:
        """Uses .grid() to place the widgets to display stats screen.

        Args:
            None.

        Returns:
            None.
        """
        self.master.resizable(1,1)
        self.master.geometry('410x245')
        self.master.resizable(0,0)
        p1Name, p2Name, gamesPlayed, wins, losses, ties = self.board.computeStats()
        self.p1NameStat.set(f"Player 1 Name (You): {p1Name}")
        self.p2NameStat.set(f"Player 2 Name: {p2Name}")
        self.gamesPlayedStat.set(f"Games Played: {gamesPlayed}")
        self.winStat.set(f"Wins: {wins}")
        self.lossStat.set(f"Losses: {losses}")
        self.tieStat.set(f"Ties: {ties}")
        self.statsTitleLabel.grid(pady=20)
        self.p1NameLabel.grid(sticky='news')
        self.p2NameLabel.grid()
        self.gamesPlayedLabel.grid()
        self.winLabel.grid()
        self.lossLabel.grid()
        self.tieLabel.grid()

    def destroyConnectionScreen(self) -> None:
        """Uses .destroy() to destroy all widgets on the connection screen.

        Args:
            None.

        Returns:
            None.
        """
        self.connectionIPLabel.destroy()
        self.connectionIPEntry.destroy()
        self.connectionPortLabel.destroy()
        self.connectionPortEntry.destroy()
        self.connectionInputButton.destroy()
        self.colonLabel.destroy()

    def destroyRequestNameScreen(self) -> None:
        """Uses .destroy() to destroy all widgets on the request name screen.

        Args:
            None.

        Returns:
            None.
        """
        self.requestNameLabel.destroy()
        self.requestNameInput.destroy()
        self.usernameButton.destroy()
        self.invalidNameLabel.destroy()

    def destroyWaitingForServerScreen(self) -> None:
        """Uses .destroy() to destroy the widget on the waiting for server screen.

        Args:
            None.

        Returns:
            None.
        """
        self.waitingForServerLabel.destroy()

    def destroyMainGame(self) -> None:
        """Uses .destroy() to destroy all widgets on the main game screen.

        Args:
            None.

        Returns:
            None.
        """
        self.playerLabel.destroy()
        self.currentTurnLabel.destroy()
        self.opponentLabel.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.btn5.destroy()
        self.btn6.destroy()
        self.btn7.destroy()
        self.btn8.destroy()
        self.btn9.destroy()

    def attemptConnection(self, ip, port) -> None:
        """The method is called when button for connecting to server is clicked.
        The method will disable the button and call connect_to_host().

        Args:
            None.

        Returns:
            None.
        """
        self.connectionInputButton['state'] = 'disabled'
        self.socket = connect_to_host(self, ip, port)

    def confirmUsername(self, p1Name) -> None:
        """This method is called when button for "Begin Game" is clicked.
        The method will use a try statement to call requestNames() from player1
        module and if it returns successfully, will set the class attribute p2Name
        to the returned value. Finally, it will call startGame() method. If exception
        is raised, an error box showing invalid username will show up and the request
        name screen will be reloaded for user to type in username again.

        Args:
            None.

        Returns:
            None.
        """
        try:
            p2Name = requestNames(self.socket, self, p1Name)
            self.p2Name.set(p2Name)
            self.startGame()
        except:
            tk.messagebox.showerror("Invalid Username", "Username can only be alphanumeric. Please try again.")
            self.destroyRequestNameScreen()
            self.createRequestNameScreen()
            self.showRequestNameScreen()

    def startGame(self) -> None:
        """This method is called when the user enters a valid username.
        The method will set the current turn to p1Name and will create a BoardClass object.
        Finally, the method will call the methods to show the main game.

        Args:
            None.

        Returns:
            None.
        """
        self.currentTurn.set(f"Current Turn: {self.p1Name.get()}")
        self.destroyRequestNameScreen()
        self.board = BoardClass(self.p1Name.get(), self.p1Name.get(), self.p2Name.get(), self.p2Name.get(), 0, 0, 0, 1)
        self.destroyWaitingForServerScreen()
        self.createMainGame()
        self.showMainGame()

    def btnClick(self, btn) -> None:
        """This method is called when any button in main game screen is clicked.
        The method will disable all buttons and check which button was clicked. Then,
        it will call the move() function from player1 module. Finally, it will update
        current turn and call checkEndGame().

        Args:
            btn (Tkinter button object): contains information on which button was clicked.

        Returns:
            None.
        """
        self.disableAllButtons()
        btn["text"] = "X"
        if(btn == self.btn1): row, col = 0, 0
        elif(btn == self.btn2): row, col = 0, 1
        elif(btn == self.btn3): row, col = 0, 2
        elif(btn == self.btn4): row, col = 1, 0
        elif(btn == self.btn5): row, col = 1, 1
        elif(btn == self.btn6): row, col = 1, 2
        elif(btn == self.btn7): row, col = 2, 0
        elif(btn == self.btn8): row, col = 2, 1
        elif(btn == self.btn9): row, col = 2, 2
        move(self.socket, self.board, row, col)
        self.board.setLastMove(self.p1Name.get())
        self.currentTurnLabel['fg'] = 'red'
        self.currentTurn.set(f"Current Turn: {self.p2Name.get()}")
        self.checkEndGame(True)

    def getServerMove(self) -> None:
        """This method is called if checkEndGame() doesn't detect a winning/tie move.
        This method will receive a move from the server and make the necessary changes
        to the current board. Finally, it will update information on current move and
        enable buttons and call checkEndGame().

        Args:
            None.

        Returns:
            None.
        """
        row, col = awaitServerMove(self.socket, self.board)
        if(row==0 and col == 0): self.btn1['text'] = 'O'
        elif(row==0 and col == 1): self.btn2['text'] = 'O'
        elif(row==0 and col == 2): self.btn3['text'] = 'O'
        elif(row==1 and col == 0): self.btn4['text'] = 'O'
        elif(row==1 and col == 1): self.btn5['text'] = 'O'
        elif(row==1 and col == 2): self.btn6['text'] = 'O'
        elif(row==2 and col == 0): self.btn7['text'] = 'O'
        elif(row==2 and col == 1): self.btn8['text'] = 'O'
        elif(row==2 and col == 2): self.btn9['text'] = 'O'
        self.board.setLastMove(self.p2Name.get())
        self.currentTurnLabel['fg'] = 'black'
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.enableButtons()
        self.checkEndGame(False)

    def disableAllButtons(self) -> None:
        """This method disables all buttons on the main game screen.

        Args:
            None.

        Returns:
            None.
        """
        self.btn1['state'] = 'disabled'
        self.btn2['state'] = 'disabled'
        self.btn3['state'] = 'disabled'
        self.btn4['state'] = 'disabled'
        self.btn5['state'] = 'disabled'
        self.btn6['state'] = 'disabled'
        self.btn7['state'] = 'disabled'
        self.btn8['state'] = 'disabled'
        self.btn9['state'] = 'disabled'

    def enableButtons(self) -> None:
        """This method enables all buttons on the main game screen.

        Args:
            None.

        Returns:
            None.
        """
        if(self.btn1['text'] == ' '): self.btn1['state'] = 'normal'
        if(self.btn2['text'] == ' '): self.btn2['state'] = 'normal'
        if(self.btn3['text'] == ' '): self.btn3['state'] = 'normal'
        if(self.btn4['text'] == ' '): self.btn4['state'] = 'normal'
        if(self.btn5['text'] == ' '): self.btn5['state'] = 'normal'
        if(self.btn6['text'] == ' '): self.btn6['state'] = 'normal'
        if(self.btn7['text'] == ' '): self.btn7['state'] = 'normal'
        if(self.btn8['text'] == ' '): self.btn8['state'] = 'normal'
        if(self.btn9['text'] == ' '): self.btn9['state'] = 'normal'

    def checkEndGame(self, getNextMove) -> None:
        """This method called .isWinner() and .boardIsFull() from the BoardClass class
        to see if the game should end.

        Args:
            getNextMove (boolean): If a button in the main game screen is clicked, getNextMove
            will be True, meaning we will call getServerMove() to get move from server. Otherwise,
            if getNextMove is False, it means a move was just received from the server and
            therefore we don't need to call getServerMove().

        Returns:
            None.
        """
        end = False
        if(self.board.isWinner()):
            if(self.board.getThisName() == self.board.getLastMove()):
                text = 'You won!'
            else:
                text = 'You lost!'
            end = True
        elif(self.board.boardIsFull()):
            text = 'Tie game!'
            end = True
        if end == True:
            cont = tk.messagebox.askquestion('Client', f"{text} Play again?", icon='info')
            if cont == 'yes':
                playAgain(self.socket, self)
            else:
                endGame(self.socket, self)
        else:
            if(getNextMove == True):
                self.getServerMove()

    def restartGame(self) -> None:
        """This method restarts the game. The method resets the game board stored in
        BoardClass and updates the numbers of games played. The method also updates the
        information on the current move. Finally, the main game screen will be regenerated.

        Args:
            None.

        Returns:
            None.
        """
        self.board.resetGameBoard()
        self.board.updateGamesPlayed()
        self.currentTurnLabel['fg'] = 'black'
        self.currentTurn.set(f"Current Turn: {self.p1Name.get()}")
        self.destroyMainGame()
        self.createMainGame()
        self.showMainGame()

    def runUI(self) -> None:
        """This method runs the mainloop for the GUI window.

        Args:
            None.

        Returns:
            None.
        """
        self.master.mainloop()

if __name__ == '__main__':
    pass