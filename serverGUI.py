import tkinter as tk
from threading import Thread
from gameboard import BoardClass

class serverGUI():
    def __init__(self):
        self.socket = object
        self.board = object
        self.p1Name = "player1"
        self.p2Name = "player2"
        self.canvasSetup()
        self.initTKVariables()
        self.createConnectionScreen()
        self.createWaitingForClientScreen()
        self.createStatScreen()
        self.showConnectionScreen()
        self.runUI()

    def initTKVariables(self):
        self.connectionIP = tk.StringVar()
        self.connectionIP.set("localhost")
        self.connectionPort = tk.IntVar()
        self.connectionPort.set(8000)
        self.p1Name = tk.StringVar()
        self.waitingText = tk.StringVar()
        self.currentTurn = tk.StringVar()
        self.messagetxt = tk.StringVar()
        self.endLabelText = tk.StringVar()
        self.p1NameStat = tk.StringVar()
        self.p2NameStat = tk.StringVar()
        self.gamesPlayedStat = tk.StringVar()
        self.winStat = tk.StringVar()
        self.lossStat = tk.StringVar()
        self.tieStat = tk.StringVar()

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("Server")
        self.master.geometry("526x570")
        self.master.resizable(1,1)

    def createConnectionScreen(self):
        self.serverIPLabel = tk.Label(self.master, text="Host Name (or IP address)", font = ("Arial, 10"))
        self.serverIPEntry = tk.Entry(self.master, textvariable=self.connectionIP, width = 30)
        self.serverPortLabel = tk.Label(self.master, text = "Port", font = ("Arial, 10"))
        self.serverPortEntry = tk.Entry(self.master, textvariable=self.connectionPort, font = ("Arial, 10"))
        self.colonLabel = tk.Label(self.master, text=":", font=("Arial, 10"))
        self.serverInputButton = tk.Button(self.master, text="Create Server", command=Thread(target=lambda:self.createServer(self.connectionIP.get(), self.connectionPort.get())).start, height=2)
        self.invalidServerLabel = tk.Label(self.master, text="Invalid server ip/port. Please try again", fg="red")

    def createWaitingForClientScreen(self):
        self.waitingForClientLabel = tk.Label(self.master, textvariable=self.waitingText, font=("Arial", 15))

    def createMainGame(self):
        self.playerLabel = tk.Label(self.master, text=f"Player Name: {self.p2Name}")
        self.currentTurnLabel = tk.Label(self.master, textvariable=self.currentTurn)
        self.opponentLabel = tk.Label(self.master, text=f"Opponent Name: {self.p1Name.get()}")
        self.btn1 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn1)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn2 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn2)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn3 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn3)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn4 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn4)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn5 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn5)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn6 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn6)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn7 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn7)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn8 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn8)).start, font=("Helvetica", 40), height=2,width=5)
        self.btn9 = tk.Button(self.master, text=" ", command = Thread(target=lambda:self.btnClick(self.btn9)).start, font=("Helvetica", 40), height=2,width=5)
        self.messagetxtLabel = tk.Label(self.master, textvariable=self.messagetxt)
        self.messagetxtLabel["fg"] = "red"
        self.disableAllButtons()

    def createStatScreen(self):
        self.statsTitleLabel = tk.Label(self.master, text = "Final Stats")
        self.p1NameLabel = tk.Label(self.master, textvariable = self.p1NameStat)
        self.p2NameLabel = tk.Label(self.master, textvariable = self.p2NameStat)
        self.gamesPlayedLabel = tk.Label(self.master, textvariable = self.gamesPlayedStat)
        self.winLabel = tk.Label(self.master, textvariable = self.winStat)
        self.lossLabel = tk.Label(self.master, textvariable = self.lossStat)
        self.tieLabel = tk.Label(self.master, textvariable = self.tieStat)
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy)

    def showConnectionScreen(self):
        self.master.geometry("348x95")
        self.master.resizable(0,0)
        self.serverIPLabel.grid(row=0,column=0, sticky="W", padx=(5,0))
        self.serverIPEntry.grid(row=1,column=0, padx=(5,0))
        self.serverPortLabel.grid(row=0,column=2, sticky="W")
        self.serverPortEntry.grid(row=1,column=2)
        self.colonLabel.grid(row=1,column=1)
        self.serverInputButton.grid(row=2, sticky="news", columnspan=3, pady=5, padx=(5,0))

    def showErrorServerScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("348x120")
        self.master.resizable(0,0)
        self.invalidServerLabel.grid(row=3,columnspan=3)

    def showWaitingForClientScreen(self):
        self.waitingForClientLabel.grid(padx=20, pady=20)

    def showMainGame(self):
        self.master.resizable(1,1)
        self.master.geometry("526x570")
        self.master.resizable(0,0)
        self.playerLabel.grid(row=0, column=0)
        self.currentTurnLabel.grid(row=0, column=1)
        self.opponentLabel.grid(row=0, column=2)
        self.btn1.grid(row=1,column=0, padx=5, pady=5)
        self.btn2.grid(row=1,column=1, padx=5, pady=5)
        self.btn3.grid(row=1,column=2, padx=5, pady=5)
        self.btn4.grid(row=2,column=0, padx=5, pady=5)
        self.btn5.grid(row=2,column=1, padx=5, pady=5)
        self.btn6.grid(row=2,column=2, padx=5, pady=5)
        self.btn7.grid(row=3,column=0, padx=5, pady=5)
        self.btn8.grid(row=3,column=1, padx=5, pady=5)
        self.btn9.grid(row=3,column=2, padx=5, pady=5)
        self.messagetxtLabel.grid(row=4,column=1)

    def showStatScreen(self):
        p1Name, p2Name, gamesPlayed, wins, losses, ties = self.board.computeStats()
        self.p1NameStat.set(f'Player 1 Name: {p1Name}')
        self.p2NameStat.set(f'Player 2 Name (You): {p2Name}')
        self.gamesPlayedStat.set(f'Games Played: {gamesPlayed}')
        self.winStat.set(f'Wins: {wins}')
        self.lossStat.set(f'Losses: {losses}')
        self.tieStat.set(f'Ties: {ties}')
        self.statsTitleLabel.grid()
        self.p1NameLabel.grid()
        self.p2NameLabel.grid()
        self.gamesPlayedLabel.grid()
        self.winLabel.grid()
        self.lossLabel.grid()
        self.tieLabel.grid()
        self.quitButton.grid()

    def hideConnectionScreen(self):
        self.serverIPLabel.grid_forget()
        self.serverIPEntry.grid_forget()
        self.serverPortLabel.grid_forget()
        self.serverPortEntry.grid_forget()
        self.serverInputButton.grid_forget()
        self.colonLabel.grid_forget()

    def hideErrorServerScreen(self):
        self.invalidServerLabel.grid_forget()

    def hideWaitingForClientScreen(self):
        self.waitingForClientLabel.grid_forget()

    def hideMainGame(self):
        self.playerLabel.grid_forget()
        self.currentTurnLabel.grid_forget()
        self.opponentLabel.grid_forget()
        self.btn1.grid_forget()
        self.btn2.grid_forget()
        self.btn3.grid_forget()
        self.btn4.grid_forget()
        self.btn5.grid_forget()
        self.btn6.grid_forget()
        self.btn7.grid_forget()
        self.btn8.grid_forget()
        self.btn9.grid_forget()
        self.messagetxtLabel.grid_forget()

    def createServer(self, ip, port):
        from player2 import createHost
        self.serverInputButton["state"] = "disabled"
        self.socket = createHost(self, ip, port)
        if(self.socket != False):
            self.startGame()

    def reloadConnectionScreen(self):
        self.invalidServerLabel.grid_forget()
        self.hideConnectionScreen()
        self.createConnectionScreen()
        self.showConnectionScreen()

    def startGame(self):
        self.hideWaitingForClientScreen()
        self.createMainGame()
        self.board = BoardClass(self.p2Name, self.p1Name.get(), self.p2Name, self.p2Name, 0, 0, 0, 1)
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.messagetxt.set(f"Waiting for {self.p1Name.get()}'s move...")
        self.messagetxtLabel['fg'] = "red"
        self.showMainGame()
        self.getClientMove()

    def getClientMove(self):
        from player2 import awaitClientMove
        row, col = awaitClientMove(self.socket, self.board)
        if(row==0 and col == 0): self.btn1["text"] = "X"
        elif(row==0 and col == 1): self.btn2["text"] = "X"
        elif(row==0 and col == 2): self.btn3["text"] = "X"
        elif(row==1 and col == 0): self.btn4["text"] = "X"
        elif(row==1 and col == 1): self.btn5["text"] = "X"
        elif(row==1 and col == 2): self.btn6["text"] = "X"
        elif(row==2 and col == 0): self.btn7["text"] = "X"
        elif(row==2 and col == 1): self.btn8["text"] = "X"
        elif(row==2 and col == 2): self.btn9["text"] = "X"
        self.board.setLastMove(self.p1Name.get())
        self.currentTurn.set(f'Current Turn: {self.p2Name}')
        self.messagetxt.set("Your turn. Make a move.")
        self.messagetxtLabel['fg'] = "black"
        self.enableButtons()
        self.checkEndGame(False)

    def btnClick(self, btn):
        from player2 import move
        self.disableAllButtons()
        btn["text"] = "O"
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
        self.board.setLastMove(self.p2Name)
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.messagetxt.set(f"Waiting for {self.p1Name.get()}'s move...")
        self.messagetxtLabel['fg'] = "red"
        self.checkEndGame(True)


    def disableAllButtons(self):
        self.btn1['state'] = 'disabled'
        self.btn2['state'] = 'disabled'
        self.btn3['state'] = 'disabled'
        self.btn4['state'] = 'disabled'
        self.btn5['state'] = 'disabled'
        self.btn6['state'] = 'disabled'
        self.btn7['state'] = 'disabled'
        self.btn8['state'] = 'disabled'
        self.btn9['state'] = 'disabled'

    def enableButtons(self):
        if(self.btn1['text'] == ' '): self.btn1['state'] = 'normal'
        if(self.btn2['text'] == ' '): self.btn2['state'] = 'normal'
        if(self.btn3['text'] == ' '): self.btn3['state'] = 'normal'
        if(self.btn4['text'] == ' '): self.btn4['state'] = 'normal'
        if(self.btn5['text'] == ' '): self.btn5['state'] = 'normal'
        if(self.btn6['text'] == ' '): self.btn6['state'] = 'normal'
        if(self.btn7['text'] == ' '): self.btn7['state'] = 'normal'
        if(self.btn8['text'] == ' '): self.btn8['state'] = 'normal'
        if(self.btn9['text'] == ' '): self.btn9['state'] = 'normal'

    def checkEndGame(self, getNextMove):
        from player2 import awaitP1Choice
        if(self.board.isWinner()):
            self.hideMainGame()
            if(self.board.getThisName() == self.board.getLastMove()):
                self.waitingText.set(f"You won!\n{self.p1Name.get()} is choosing if they want to play again...")
            else:
                self.waitingText.set(f"You lost!\n{self.p1Name.get()} is choosing if they want to play again...")
            self.showWaitingForClientScreen()
            awaitP1Choice(self.socket, self)
        elif(self.board.boardIsFull()):
            self.hideMainGame()
            self.waitingText.set(f"Tie game!\n{self.p1Name.get()} is choosing if they want to play again...")
            self.showWaitingForClientScreen()
            awaitP1Choice(self.socket, self)
        else:
            if(getNextMove == True):
                self.getClientMove()

    def restartGame(self):
        self.board.resetGameBoard()
        self.board.updateGamesPlayed()
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.messagetxt.set(f"Waiting for {self.p1Name.get()}'s move...")
        self.createMainGame()
        self.showMainGame()
        self.getClientMove()

    def runUI(self):
        self.master.mainloop()

def runServer():
    gui = serverGUI()

if __name__ == "__main__":
    runServer()