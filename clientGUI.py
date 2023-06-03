import tkinter as tk
from tkinter import font
from threading import Thread
from player1 import *
from gameboard import BoardClass

class clientServer():
    def __init__(self):
        self.socket = object
        self.board = object
        self.p1Name = "player1"
        self.p2Name = "player2"
        self.font = ("Small Fonts", 13)
        self.canvasSetup()
        self.initTKVariables()
        self.createConnectionScreen()
        self.createErrorClientScreen()
        self.createRequestNameScreen()
        self.createEndScreen()
        self.createStatScreen()
        self.showConnectionScreen()
        self.runUI()

    def initTKVariables(self):
        self.connectionIP = tk.StringVar()
        self.connectionIP.set("localhost")
        self.connectionPort = tk.StringVar()
        self.connectionPort.set("8000")
        self.p1Name = tk.StringVar()
        self.currentTurn = tk.StringVar()
        self.endLabelText = tk.StringVar()
        self.p1NameStat = tk.StringVar()
        self.p2NameStat = tk.StringVar()
        self.gamesPlayedStat = tk.StringVar()
        self.winStat = tk.StringVar()
        self.lossStat = tk.StringVar()
        self.tieStat = tk.StringVar()

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("Client")
        self.master.geometry("526x570")
        self.master.resizable(1,1)

    def createConnectionScreen(self):
        self.connectionIPLabel = tk.Label(self.master, text="Host Name (or IP address)", font=self.font)
        self.connectionIPEntry = tk.Entry(self.master, textvariable=self.connectionIP, font=self.font, width=25)
        self.connectionPortLabel = tk.Label(self.master, text = "Port", font =self.font)
        self.connectionPortEntry = tk.Entry(self.master, textvariable=self.connectionPort, font=self.font, width=15)
        self.colonLabel = tk.Label(self.master, text=":", font=self.font)
        self.connectionInputButton = tk.Button(self.master, text="Connect", font=self.font, command=Thread(target=lambda:self.attemptConnection(self.connectionIP.get(), self.connectionPort.get())).start, height=2)

    def createErrorClientScreen(self):
        self.invalidConnectionLabel = tk.Label(self.master, text="Connection could not be made. Try again?", fg="red", font=self.font)
        self.yesButton = tk.Button(self.master, text="Yes", command=lambda:[self.showConnectionScreen(), self.hideErrorClientScreen()], font=self.font)
        self.noButton = tk.Button(self.master, text="No", command = self.master.destroy, font=self.font)

    def createRequestNameScreen(self):
        self.requestNameLabel = tk.Label(self.master, text="Please enter your username (only alphanumeric):", font=self.font)
        self.requestNameInput = tk.Entry(self.master, textvariable=self.p1Name, font=self.font)
        self.usernameButton = tk.Button(self.master, text="Begin Game", command=Thread(target=lambda:self.confirmUsername(self.p1Name.get())).start, font=self.font, height=2)
        self.invalidNameLabel = tk.Label(self.master, text="Username can only be alphanumeric. Please try again.", fg="red", font=self.font)

    def createMainGame(self):
        self.playerLabel = tk.Label(self.master, text=f"Your Name: {self.p1Name.get()}", font=self.font)
        self.currentTurnLabel = tk.Label(self.master, textvariable=self.currentTurn, font=("Small Fonts", 15))
        self.opponentLabel = tk.Label(self.master, text=f"Opponent Name: {self.p2Name}", font=self.font)
        self.btn1 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn1)).start, height=2, width=5)
        self.btn2 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn2)).start, height=2, width=5)
        self.btn3 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn3)).start, height=2, width=5)
        self.btn4 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn4)).start, height=2, width=5)
        self.btn5 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn5)).start, height=2, width=5)
        self.btn6 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn6)).start, height=2, width=5)
        self.btn7 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn7)).start, height=2, width=5)
        self.btn8 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn8)).start, height=2, width=5)
        self.btn9 = tk.Button(self.master, text=" ", font=("Small Fonts", 40), command = Thread(target=lambda:self.btnClick(self.btn9)).start, height=2, width=5)

    def createEndScreen(self):
        self.endLabel = tk.Label(self.master, textvariable=self.endLabelText, font=self.font)
        self.continueButton = tk.Button(self.master, text="Yes", command=lambda:[playAgain(self.socket, self), self.hideEndScreen()], font=self.font)
        self.stopButton = tk.Button(self.master, text="No", command=lambda:[endGame(self.socket, self), self.hideEndScreen()], font=self.font)

    def createStatScreen(self):
        self.statsTitleLabel = tk.Label(self.master, text="Final Stats", font=self.font, fg="red")
        self.p1NameLabel = tk.Label(self.master, textvariable=self.p1NameStat, font=self.font, width=40)
        self.p2NameLabel = tk.Label(self.master, textvariable=self.p2NameStat, font=self.font)
        self.gamesPlayedLabel = tk.Label(self.master, textvariable=self.gamesPlayedStat, font=self.font)
        self.winLabel = tk.Label(self.master, textvariable=self.winStat, font=self.font)
        self.lossLabel = tk.Label(self.master, textvariable=self.lossStat, font=self.font)
        self.tieLabel = tk.Label(self.master, textvariable=self.tieStat, font=self.font)

    def showConnectionScreen(self):
        self.connectionInputButton["state"] = "normal"
        self.master.geometry("459x152")
        self.master.resizable(0,0)
        self.connectionIPLabel.grid(row=0,column=0, sticky="W", padx=(20,0), pady=(20,0))
        self.connectionIPEntry.grid(row=1,column=0, padx=(20,0))
        self.connectionPortLabel.grid(row=0,column=2, sticky="W", pady=(20,0))
        self.connectionPortEntry.grid(row=1,column=2)
        self.colonLabel.grid(row=1,column=1)
        self.connectionInputButton.grid(row=2, sticky="news", columnspan=3, pady=5, padx=(20,0))

    def showErrorClientScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("350x110")
        self.master.resizable(0,0)
        self.invalidConnectionLabel.grid(columnspan=2, padx=20, pady=(20, 5))
        self.yesButton.grid(row=1, column=0, padx=(20,5), sticky="news")
        self.noButton.grid(row=1, column=1, padx=(5,20), sticky="news")

    def showRequestNameScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("387x158")
        self.master.resizable(0,0)
        self.requestNameLabel.grid(row=0,column=0, padx=20,pady=(20,0))
        self.requestNameInput.grid(row=1, sticky="news", padx=20, pady=(0,5))
        self.usernameButton.grid(row=2, sticky="news", padx=20)

    def showMainGame(self):
        self.master.resizable(1,1)
        self.master.geometry("522x590")
        self.master.resizable(0,0)
        self.playerLabel.grid(row=0, column=0, columnspan=2, padx=(10,0), sticky="W")
        self.opponentLabel.grid(row=0, column=1, columnspan=2, sticky="E")
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

    def showEndScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("205x111")
        self.master.resizable(0,0)
        self.endLabel.grid(row=0, columnspan=2, padx=20, pady=(20, 5))
        self.continueButton.grid(row=1, column=0, padx=(20,5), sticky="news")
        self.stopButton.grid(row=1, column=1, padx=(5,20), sticky="news")

    def showStatScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("410x245")
        self.master.resizable(0,0)
        p1Name, p2Name, gamesPlayed, wins, losses, ties = self.board.computeStats()
        self.p1NameStat.set(f'Player 1 Name (You): {p1Name}')
        self.p2NameStat.set(f'Player 2 Name: {p2Name}')
        self.gamesPlayedStat.set(f'Games Played: {gamesPlayed}')
        self.winStat.set(f'Wins: {wins}')
        self.lossStat.set(f'Losses: {losses}')
        self.tieStat.set(f'Ties: {ties}')
        self.statsTitleLabel.grid(pady=20)
        self.p1NameLabel.grid(sticky="news")
        self.p2NameLabel.grid()
        self.gamesPlayedLabel.grid()
        self.winLabel.grid()
        self.lossLabel.grid()
        self.tieLabel.grid()

    def hideConnectionScreen(self):
        self.connectionIPLabel.grid_forget()
        self.connectionIPEntry.grid_forget()
        self.connectionPortLabel.grid_forget()
        self.connectionPortEntry.grid_forget()
        self.connectionInputButton.grid_forget()
        self.colonLabel.grid_forget()

    def hideErrorClientScreen(self):
        self.invalidConnectionLabel.grid_forget()
        self.yesButton.grid_forget()
        self.noButton.grid_forget()

    def hideRequestNameScreen(self):
        self.requestNameLabel.grid_forget()
        self.requestNameInput.grid_forget()
        self.usernameButton.grid_forget()
        self.invalidNameLabel.grid_forget()

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

    def hideEndScreen(self):
        self.endLabel.grid_forget()
        self.continueButton.grid_forget()
        self.stopButton.grid_forget()

    def attemptConnection(self, ip, port):
        self.connectionInputButton["state"] = "disabled"
        self.socket = connect_to_host(self, ip, port)

    def confirmUsername(self, p1Name):
        try:
            requestNames(self.socket, p1Name)
            self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
            self.hideRequestNameScreen()
            self.board = BoardClass(self.p1Name.get(), self.p1Name.get(), self.p2Name, self.p2Name, 0, 0, 0, 1)
            self.createMainGame()
            self.showMainGame()
        except:
            self.hideRequestNameScreen()
            self.createRequestNameScreen()
            self.showRequestNameScreen()
            self.invalidNameLabel.grid(row=3)

    def btnClick(self, btn):
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
        self.currentTurnLabel['fg'] = "red"
        self.currentTurn.set(f'Current Turn: {self.p2Name}')
        self.checkEndGame(True)

    def getServerMove(self):
        row, col = awaitServerMove(self.socket, self.board)
        if(row==0 and col == 0): self.btn1["text"] = "O"
        elif(row==0 and col == 1): self.btn2["text"] = "O"
        elif(row==0 and col == 2): self.btn3["text"] = "O"
        elif(row==1 and col == 0): self.btn4["text"] = "O"
        elif(row==1 and col == 1): self.btn5["text"] = "O"
        elif(row==1 and col == 2): self.btn6["text"] = "O"
        elif(row==2 and col == 0): self.btn7["text"] = "O"
        elif(row==2 and col == 1): self.btn8["text"] = "O"
        elif(row==2 and col == 2): self.btn9["text"] = "O"
        self.board.setLastMove(self.p2Name)
        self.currentTurnLabel['fg'] = "black"
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.enableButtons()
        self.checkEndGame(False)

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
        if(self.board.isWinner()):
            self.hideMainGame()
            if(self.board.getThisName() == self.board.getLastMove()):
                self.endLabelText.set("You won! Play again?")
            else:
                self.endLabelText.set("You lost! Play again?")
            self.showEndScreen()
        elif(self.board.boardIsFull()):
            self.hideMainGame()
            self.endLabelText.set("Tie game! Play again?")
            self.showEndScreen()
        else:
            if(getNextMove == True):
                self.getServerMove()

    def restartGame(self):
        self.board.resetGameBoard()
        self.board.updateGamesPlayed()
        self.currentTurnLabel['fg'] = "black"
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.createMainGame()
        self.showMainGame()

    def runUI(self):
        self.master.mainloop()

def runClient():
    gui = clientServer()

if __name__ == "__main__":
    runClient()