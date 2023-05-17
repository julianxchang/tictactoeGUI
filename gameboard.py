"""WHY YOU STILL LOOKING AT MY CODE"""



































































































class BoardClass:
    """A class to store and handle information about the current tictactoe board.

    Attributes:
        name (str): The name of the player.
        lastMove (str): The name of player who last moved.
        numWins (int): The total number of wins.
        numTies (int): The total number of ties.
        numLosses (int): The total number of losses.
        gamesPlayed (int): The total number of games played.
        board (list): The current board.
    """
    
    def __init__(self, name: str = "", lastMove: str = "", numWins: int = 0, numTies: int = 0, numLosses: int = 0, gamesPlayed: int = 0, board: list = [[" "," "," "],[" "," "," "],[" "," "," "]]):
        """Creates a BoardClass with all the information of the board.
        
        Args:
            name: The name of the player.
            lastMove: The name of player who last moved.
            numWins: The total number of wins.
            numTies: The total number of ties.
            numLosses: The total number of losses.
            gamesPlayed: The total number of games played.
            board: The current board.

        Returns:
            None.
        """
        self.setName(name)
        self.setLastMove(lastMove)
        self.setNumWins(numWins)
        self.setNumTies(numTies)
        self.setNumLosses(numLosses)
        self.setBoard(board)
        self.setGamesPlayed(gamesPlayed)
    
    def setName(self, name: str) -> None:
        """Sets the name of the player.
        
        Args:
            name: Name of the player.

        Returns:
            None.
        """
        self.name = name

    def setLastMove(self, lastMove: str) -> None:
        """Sets the name of the player who last moved.
        
        Args:
            lastMove: The name of player who last moved.
        
        Returns:
            None.
        """
        self.lastMove = lastMove

    def setNumWins(self, numWins: str) -> None:
        """Sets the number of wins.
        
        Args:
            numWins: The total number of wins.

        Returns:
            None.
        """
        self.numWins = numWins

    def setNumTies(self, numTies: str) -> None:
        """Sets the number of ties.
        
        Args:
            numTies: The total number of ties.

        Returns:
            None.
        """
        self.numTies = numTies

    def setNumLosses(self, numLosses: str) -> None:
        """Sets the number of wins.
        
        Args:
            numLosses: The total number of losses.

        Returns:
            None.
        """
        self.numLosses = numLosses

    def setGamesPlayed(self, gamesPlayed: str) -> None:
        """Sets the number of games played.

        Args:
            gamesPlayed: The total number of games played.

        Returns:
            None.
        """
        self.gamesPlayed = gamesPlayed

    def setBoard(self, board: str) -> None:
        """Sets the current board.

        Args:
            board: The current board.

        Returns:
            None.
        """
        self.board = board

    def getName(self) -> str:
        """Gets the name of the player.

        Args:
            None.

        Returns:
            A copy of the attribute name.

        """
        return self.name
    
    def getLastMove(self) -> str:
        """Gets the name of the player who last moved.

        Args:
            None.

        Returns:
            A copy of the attribute lastMove.
        """
        return self.lastMove
    
    def getNumWins(self) -> int:
        """Gets the total number of wins.

        Args:
            None.

        Returns:
            A copy of the attribute numWins.
        """
        return self.numWins
    
    def getNumTies(self) -> int:
        """Gets the total number of ties.

        Args:
            None.

        Returns:
            A copy of the attribute numTies.
        """
        return self.numTies
    
    def getNumLosses(self) -> int:
        """Gets the total number of losses.

        Args:
            None.

        Returns:
            A copy of the attribute numLosses.
        """
        return self.numLosses

    def getGamesPlayed(self) -> int:
        """Gets the total number of games played.

        Args:
            None.

        Returns:
            A copy of the attribute gamedPlayed.
        """
        return self.gamesPlayed

    def updateGamesPlayed(self) -> None:
        """Updates the number of games played by one.

        Args:
            None.

        Returns:
            None.
        """
        self.setGamesPlayed(self.getGamesPlayed() + 1)

    def resetGameBoard(self):
        """Resets the gameboard.

        Using the setBoard() function, this function will
        set the board to the default state. This function
        also sets the attribute lastMove to "player2"

        Args:
            None.

        Returns:
            None.
        """
        self.setBoard([[" "," "," "],[" "," "," "],[" "," "," "]])
        self.setLastMove("player2")

    def isEmpty(self, row, col):
        """Checks if a specific space is already taken on the board.

        Args:
            row: row of the board.
            col: column of the board.

        Returns:
            True: specified space is not taken.
            False: specified space is taken.
        """
        if(self.board[row][col] == " "):
            return True
        return False

    def updateGameBoard(self, row, col):
        """Updates the board with the corresponding row/col.

        If the attribute lastMove equals "player2", the corresponding
        row and column of the board will equal "X". Otherwise, it would
        be "O" 

        Args:
            row: row of the board.
            col: column of the board.

        Returns:
            None.
        """
        if self.getLastMove() == "player2":
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"
    
    def isWinner(self):
        """Checks if the current board contains a winning move.

        Checks current board twice, each time with token = "X" and token = "O"
        to see if any player has made a winning move. If a winning move is found,
        this function will increment attribute numWins by 1 if the attribute name 
        equals the attribute lastMove. Otherwise, the attribute numLosses will
        increment by 1.


        Args:
            None.

        Returns:
            True: There is a winning move on the board.
            False: There are no winning moves on the board.
        """
        win = False
        token = ""
        for i in range(2):
            if(i == 0):
                token = "X"
            else:
                token = "O"
            #Check for horizontal
            for row in range(3):
                if self.board[row].count(token) == 3:
                    win = True
            #Check for vertical
            for col in range(3):
                if self.board[0][col] == token and self.board[1][col] == token and self.board[2][col] == token:
                    win = True
            #Check for diagonal
            if(self.board[0][0] == token and self.board[1][1] == token and self.board[2][2] == token):
                win = True
            if(self.board[0][2] == token and self.board[1][1] == token and self.board[2][0] == token):
                win = True
        
        #Check if win detected
        if win == True:
            if self.getName() == self.getLastMove():
                self.setNumWins(self.getNumWins() + 1)
                print("You Won!")
                return True
            else:
                self.setNumLosses(self.getNumLosses() + 1)
                print("You Lost!")
                return True
        return False

    

    def boardIsFull(self) -> bool:
        """Checks if the current board is full

        Loops through the current board and returns False if 
        there is a space found (empty space). If no space is 
        found, the attribute numTies will be incremented by 1.

        Args:
            None.

        Returns:
            True: The board is full
            False: The board is not full
        """
        for row in self.board:
            if row.count(" ") != 0:
                return False
        self.setNumTies(self.getNumTies() + 1)
        print("Tie Game!")
        return True

    def printStats(self):
        """Prints the stats.

        This function will print the players name, last person 
        to make a move, total games played, and number of wins, 
        ties, and losses.

        Args:
            None.

        Returns:
            None.
        """
        print()
        print("Final Stats\n-----------------------")
        print("Player Name:", self.getName())
        print("Last person to make move:", self.getLastMove())
        print("Total Games Played:", self.getGamesPlayed())
        print("Wins:", self.getNumWins())
        print("Ties:", self.getNumTies())
        print("Losses:", self.getNumLosses())

    def printBoard(self):
        """Prints the current board

        Args:
            None.

        Returns:
            None.
        """
        i = 0
        for row in self.board:
            print(" | ".join(row))
            if(i<2):
                print("---------")
            i += 1
