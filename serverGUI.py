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
        self.createEndScreen()
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
        self.endLabelText = tk.StringVar()

    def canvasSetup(self):
        self.master = tk.Tk()
        self.master.title("Server")
        self.master.geometry("526x547")
        self.master.resizable(0,0)

    def createConnectionScreen(self):
        self.label1 = tk.Label(self.master, text="Enter host ip address:")
        self.connectionIPEntry = tk.Entry(self.master, textvariable=self.connectionIP)
        self.label2 = tk.Label(self.master, text = "Enter host port number:")
        self.connectionPortEntry = tk.Entry(self.master, textvariable=self.connectionPort)
        self.connectionInputButton = tk.Button(self.master, text="Create Server", command=Thread(target=lambda:self.attemptCreateServer(self.connectionIP.get(), self.connectionPort.get())).start)
        self.label3 = tk.Label(self.master, text="Invalid server ip/port. Please try again", fg="red")

    def showConnectionScreen(self):
        self.label1.grid(row=0,column=0)
        self.connectionIPEntry.grid(row=0,column=1, padx=55)
        self.label2.grid(row=1,column=0)
        self.connectionPortEntry.grid(row=1,column=1, padx=55)
        self.connectionInputButton.grid(row=2)

    def destroyConnectionScreen(self):
        self.label1.destroy()
        self.connectionIPEntry.destroy()
        self.label2.destroy()
        self.connectionPortEntry.destroy()
        self.connectionInputButton.destroy()

    def attemptCreateServer(self, ip, port):
        from player2 import createHost
        self.connectionInputButton["state"] = "disabled"
        self.socket = createHost(self, ip, port)
        self.destroyWaitingForClientScreen()
        self.createMainGame()
        self.board = BoardClass(self.p2Name, self.p1Name.get(), self.p2Name, self.p2Name, 0, 0, 0, 0)
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.showMainGame()
        self.getClientMove()

    def getClientMove(self):
        from player2 import awaitClientMove
        row, col = awaitClientMove(self.socket, self.board)
        if(row==0 and col == 0):
            self.btn1["text"] = "X"
        elif(row==0 and col == 1):
            self.btn2["text"] = "X"
        elif(row==0 and col == 2):
            self.btn3["text"] = "X"
        elif(row==1 and col == 0):
            self.btn4["text"] = "X"
        elif(row==1 and col == 1):
            self.btn5["text"] = "X"
        elif(row==1 and col == 2):
            self.btn6["text"] = "X"
        elif(row==2 and col == 0):
            self.btn7["text"] = "X"
        elif(row==2 and col == 1):
            self.btn8["text"] = "X"
        elif(row==2 and col == 2):
            self.btn9["text"] = "X"
        self.board.setLastMove(self.p1Name.get())
        self.currentTurn.set(f'Current Turn: {self.p2Name}')
        self.enableButtons()
        self.checkEndGame()

    def createWaitingForClientScreen(self):
        self.waitingForClientLabel = tk.Label(self.master, textvariable=self.waitingText)

    def showWaitingForClientScreen(self):
        self.waitingForClientLabel.grid()

    def destroyWaitingForClientScreen(self):
        self.waitingForClientLabel.destroy()

    def showErrorServerScreen(self):
        self.label3.grid(row=2,column=1)

    def reloadConnectionScreen(self):
        self.label3.destroy()
        self.destroyConnectionScreen()
        self.createConnectionScreen()
        self.showConnectionScreen()

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
        self.disableAllButtons()

    def destroyMainGame(self):
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

    def btnClick(self, btn):
        from player2 import move
        self.disableAllButtons()
        btn["text"] = "O"
        if(btn == self.btn1):
            row, col = 0, 0
        elif(btn == self.btn2):
            row, col = 0, 1
        elif(btn == self.btn3):
            row, col = 0, 2
        elif(btn == self.btn4):
            row, col = 1, 0
        elif(btn == self.btn5):
            row, col = 1, 1
        elif(btn == self.btn6):
            row, col = 1, 2
        elif(btn == self.btn7):
            row, col = 2, 0
        elif(btn == self.btn8):
            row, col = 2, 1
        elif(btn == self.btn9):
            row, col = 2, 2
        move(self.socket, self.board, row, col)
        self.board.setLastMove(self.p2Name)
        self.currentTurn.set(f'Current Turn: {self.p1Name.get()}')
        self.checkEndGame()
        self.getClientMove()

    def showMainGame(self):
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
        if(self.btn1['text'] == ' '):
            self.btn1['state'] = 'normal'
        if(self.btn2['text'] == ' '):
            self.btn2['state'] = 'normal'
        if(self.btn3['text'] == ' '):
            self.btn3['state'] = 'normal'
        if(self.btn4['text'] == ' '):
            self.btn4['state'] = 'normal'
        if(self.btn5['text'] == ' '):
            self.btn5['state'] = 'normal'
        if(self.btn6['text'] == ' '):
            self.btn6['state'] = 'normal'
        if(self.btn7['text'] == ' '):
            self.btn7['state'] = 'normal'
        if(self.btn8['text'] == ' '):
            self.btn8['state'] = 'normal'
        if(self.btn9['text'] == ' '):
            self.btn9['state'] = 'normal'

    def createEndScreen(self):
        self.endLabel = tk.Label(self.master, textvariable=self.endLabelText)

    def showEndScreen(self):
        self.endLabel.grid(row=0, column=0)

    def destroyEndScreen(self):
        self.endLabel.destroy()
        self.continueButton.destroy()
        self.stopButton.destroy()

    def checkEndGame(self):
        from player2 import playAgain
        if(self.board.isWinner()):
            self.destroyMainGame()
            if(self.board.getThisName() == self.board.getLastMove()):
                self.endLabelText.set(f"You won! {self.p1Name.get()} is choosing if they want to play again...")
            else:
                self.endLabelText.set(f"You lost! {self.p1Name.get()} is choosing if they want to play again...")
            self.showEndScreen()
            playAgain(self.socket, self)
        if(self.board.boardIsFull()):
            self.destroyMainGame()
            self.endLabelText.set(f"Tie game! {self.p1Name.get()} is choosing if they want to play again...")
            self.showEndScreen()
            playAgain(self.socket, self)


    def restartGame(self):
        self.board.resetGameBoard()
        self.createMainGame()
        self.showMainGame()

    def createStatScreen(self):
        pass

    def showStatScreen(self):
        print("Hit")


    def runUI(self):
        self.master.mainloop()



def runServer():
    gui = serverGUI()

if __name__ == "__main__":
    runServer()