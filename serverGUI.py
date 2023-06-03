import tkinter as tk
from tkinter import messagebox
from threading import Thread
from gameboard import BoardClass
from player2 import *

class serverGUI():
    def __init__(self):
        self.socket = object
        self.board = object
        self.p1Name = "player1"
        self.p2Name = "player2"
        self.font = ("Small Fonts", 13)
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
        self.connectionPort = tk.StringVar()
        self.connectionPort.set("8000")
        self.p1Name = tk.StringVar()
        self.waitingText = tk.StringVar()
        self.currentTurn = tk.StringVar()
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
        self.serverIPLabel = tk.Label(self.master, text="Host Name (or IP address)", font=self.font)
        self.serverIPEntry = tk.Entry(self.master, textvariable=self.connectionIP, font=self.font, width = 25)
        self.serverPortLabel = tk.Label(self.master, text = "Port", font=self.font)
        self.serverPortEntry = tk.Entry(self.master, textvariable=self.connectionPort, font=self.font, width=15)
        self.colonLabel = tk.Label(self.master, text=":", font=self.font)
        self.serverInputButton = tk.Button(self.master, text="Create Server", font=self.font, command=Thread(target=lambda:self.createServer(self.connectionIP.get(), self.connectionPort.get())).start, height=2)
        self.invalidServerLabel = tk.Label(self.master, text="Invalid server ip/port. Please try again", font=self.font, fg="red")

    def createWaitingForClientScreen(self):
        self.waitingForClientLabel = tk.Label(self.master, textvariable=self.waitingText, font=self.font)

    def createMainGame(self):
        self.playerLabel = tk.Label(self.master, text=f"Player Name: {self.p2Name}", font=self.font)
        self.currentTurnLabel = tk.Label(self.master, textvariable=self.currentTurn, font=("Small Fonts", 15), fg="red")
        self.opponentLabel = tk.Label(self.master, text=f"Opponent Name: {self.p1Name.get()}", font=self.font)
        self.btn1 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn1)).start, height=2,width=5)
        self.btn2 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn2)).start, height=2,width=5)
        self.btn3 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn3)).start, height=2,width=5)
        self.btn4 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn4)).start, height=2,width=5)
        self.btn5 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn5)).start, height=2,width=5)
        self.btn6 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn6)).start, height=2,width=5)
        self.btn7 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn7)).start, height=2,width=5)
        self.btn8 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn8)).start, height=2,width=5)
        self.btn9 = tk.Button(self.master, text=" ", font=("Small FOnts", 40), command = Thread(target=lambda:self.btnClick(self.btn9)).start, height=2,width=5)
        self.disableAllButtons()

    def createStatScreen(self):
        self.statsTitleLabel = tk.Label(self.master, text="Final Stats", font=self.font, fg="red")
        self.p1NameLabel = tk.Label(self.master, textvariable=self.p1NameStat, font=self.font, width=40)
        self.p2NameLabel = tk.Label(self.master, textvariable=self.p2NameStat, font=self.font)
        self.gamesPlayedLabel = tk.Label(self.master, textvariable=self.gamesPlayedStat, font=self.font)
        self.winLabel = tk.Label(self.master, textvariable=self.winStat, font=self.font)
        self.lossLabel = tk.Label(self.master, textvariable=self.lossStat, font=self.font)
        self.tieLabel = tk.Label(self.master, textvariable=self.tieStat, font=self.font)

    def showConnectionScreen(self):
        self.master.geometry("459x152")
        self.master.resizable(0,0)
        self.serverIPLabel.grid(row=0,column=0, sticky="W", padx=(20,0), pady=(20,0))
        self.serverIPEntry.grid(row=1,column=0, padx=(20,0))
        self.serverPortLabel.grid(row=0,column=2, sticky="W", pady=(20,0))
        self.serverPortEntry.grid(row=1,column=2)
        self.colonLabel.grid(row=1,column=1)
        self.serverInputButton.grid(row=2, sticky="news", columnspan=3, pady=5, padx=(20,0))

    def showErrorServerMessageBox(self):
        tk.messagebox.showerror("Error", "Server could not be created. Please try again.")
        self.hideConnectionScreen()
        self.createConnectionScreen()
        self.showConnectionScreen()

    def showSuccessfulServerScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("240x90")
        self.master.resizable(0,0)
        self.waitingText.set(f"Waiting for connection on:\n{self.connectionIP.get()}:{self.connectionPort.get()}")
        self.hideConnectionScreen()
        self.hideErrorServerScreen()
        self.showWaitingForClientScreen()

    def showWaitingForClientScreen(self):
        self.waitingForClientLabel.grid(padx=20, pady=20)

    def showClientConnectedScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("315x90")
        self.master.resizable(0,0)
        self.waitingText.set("Client connected!\nWaiting for them to input username...")

    def showMainGame(self):
        self.master.resizable(1,1)
        self.master.geometry("522x590")
        self.master.resizable(0,0)
        self.playerLabel.grid(row=0, column=0, columnspan=2, padx=(10,0), sticky="W")
        self.opponentLabel.grid(row=0, column=1, columnspan=2, sticky="E")
        self.btn1.grid(row=1,column=0, padx=(10,5), pady=5)
        self.btn2.grid(row=1,column=1, padx=5, pady=5)
        self.btn3.grid(row=1,column=2, padx=5, pady=5)
        self.btn4.grid(row=2,column=0, padx=(10,5), pady=5)
        self.btn5.grid(row=2,column=1, padx=5, pady=5)
        self.btn6.grid(row=2,column=2, padx=5, pady=5)
        self.btn7.grid(row=3,column=0, padx=(10,5), pady=5)
        self.btn8.grid(row=3,column=1, padx=5, pady=5)
        self.btn9.grid(row=3,column=2, padx=5, pady=5)
        self.currentTurnLabel.grid(row=4, columnspan=3)

    def showStatScreen(self):
        self.master.resizable(1,1)
        self.master.geometry("410x245")
        self.master.resizable(0,0)
        p1Name, p2Name, gamesPlayed, wins, losses, ties = self.board.computeStats()
        self.p1NameStat.set(f'Player 1 Name: {p1Name}')
        self.p2NameStat.set(f'Player 2 Name (You): {p2Name}')
        self.gamesPlayedStat.set(f'Games Played: {gamesPlayed}')
        self.winStat.set(f'Wins: {wins}')
        self.lossStat.set(f'Losses: {losses}')
        self.tieStat.set(f'Ties: {ties}')
        self.statsTitleLabel.grid(pady=20)
        self.p1NameLabel.grid()
        self.p2NameLabel.grid()
        self.gamesPlayedLabel.grid()
        self.winLabel.grid()
        self.lossLabel.grid()
        self.tieLabel.grid()

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

    def createServer(self, ip, port):
        self.serverInputButton["state"] = "disabled"
        self.socket = createHost(self, ip, port)
        if(self.socket != False):
            self.startGame()

    def startGame(self):
        self.hideWaitingForClientScreen()
        self.createMainGame()
        self.board = BoardClass(self.p2Name, self.p1Name.get(), self.p2Name, self.p2Name, 0, 0, 0, 1)
        self.currentTurnLabel["fg"] = "red"
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.showMainGame()
        self.getClientMove('none')

    def getClientMove(self, move):
        if(move == 'none'):
            row, col = awaitClientMove(self.socket, self.board)
        else:
            self.hideMainGame()
            self.createMainGame()
            self.showMainGame()
            row, col = int(move[0]), int(move[1])
            self.board.updateGameBoard(row, col)
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
        self.currentTurnLabel["fg"] = "black"
        self.currentTurn.set(f'Current Turn: {self.p2Name}')
        self.enableButtons()
        self.checkEndGame(False)

    def btnClick(self, btn):
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
        self.currentTurnLabel["fg"] = "red"
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
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
        end = False
        if(self.board.isWinner()):
            if(self.board.getThisName() == self.board.getLastMove()):
                title = "Winner!"
                text= f"You won!\n{self.p1Name.get()} is choosing if they want to play again..."
            else:
                title = "Loser."
                text = f"You lost!\n{self.p1Name.get()} is choosing if they want to play again..."
            end = True
        elif(self.board.boardIsFull()):
            text= f"Tie game!\n{self.p1Name.get()} is choosing if they want to play again..."
            end = True
        if end == True:
            self.disableAllButtons()
            tk.messagebox.showinfo(title, text)
            awaitP1Choice(self.socket, self)
        else:
            if(getNextMove == True):
                self.getClientMove('none')

    def restartGame(self, move):
        self.board.resetGameBoard()
        self.board.updateGamesPlayed()
        self.currentTurnLabel["fg"] = "red"
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        if(move == 'none'):
            self.hideMainGame()
            self.createMainGame()
            self.showMainGame()
            self.getClientMove('none')
        else:
            self.getClientMove(move)

    def runUI(self):
        self.master.mainloop()

def runServer():
    gui = serverGUI()

if __name__ == "__main__":
    runServer()