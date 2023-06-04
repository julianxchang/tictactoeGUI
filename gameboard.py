class BoardClass:
    """A class to store and handle information about the current tictactoe board.

    Attributes:
        name (str): The name of the player.
        last_move (str): The name of player who last moved.
        num_wins (int): The total number of wins.
        num_ties (int): The total number of ties.
        num_losses (int): The total number of losses.
        total_games (int): The total number of games played.
        board (list): The current board.
    """

    def __init__(self, thisName: str = "", p1Name: str = "", p2Name: str = "", last_move: str = "", num_wins: int = 0, num_ties: int = 0, num_losses: int = 0, games_played: int = 0, board: list = [[" "," "," "],[" "," "," "],[" "," "," "]]):
        """Creates a BoardClass with all the information of the board.

        Args:
            name: The name of the player.
            last_move: The name of player who last moved.
            num_wins: The total number of wins.
            num_ties: The total number of ties.
            num_losses: The total number of losses.
            total_games: The total number of games played.
            board: The current board.

        Returns:
            None.
        """
        self.setThisName(thisName)
        self.setP1Name(p1Name)
        self.setP2Name(p2Name)
        self.setLastMove(last_move)
        self.setNumWins(num_wins)
        self.setNumTies(num_ties)
        self.setNumLosses(num_losses)
        self.setGamesPlayed(games_played)
        self.setBoard(board)

    def setThisName(self, thisName: str) -> None:
        self.thisName = thisName

    def setP1Name(self, name: str) -> None:
        """Sets the name of the player.

        Args:
            name: Name of the player.

        Returns:
            None.
        """
        self.p1Name = name

    def setP2Name(self, name: str) -> None:
        """Sets the name of the player.

        Args:
            name: Name of the player.

        Returns:
            None.
        """
        self.p2Name = name

    def setLastMove(self, last_move: str) -> None:
        """Sets the name of the player who last moved.

        Args:
            last_move: The name of player who last moved.

        Returns:
            None.
        """
        self.last_move = last_move

    def setNumWins(self, num_wins: str) -> None:
        """Sets the number of wins.

        Args:
            num_wins: The total number of wins.

        Returns:
            None.
        """
        self.num_wins = num_wins

    def setNumTies(self, num_ties: str) -> None:
        """Sets the number of ties.

        Args:
            num_ties: The total number of ties.

        Returns:
            None.
        """
        self.num_ties = num_ties

    def setNumLosses(self, num_losses: str) -> None:
        """Sets the number of wins.

        Args:
            num_losses: The total number of losses.

        Returns:
            None.
        """
        self.num_losses = num_losses

    def setGamesPlayed(self, games_played: str) -> None:
        """Sets the number of games played.

        Args:
            total_games: The total number of games played.

        Returns:
            None.
        """
        self.games_played = games_played

    def setBoard(self, board: str) -> None:
        """Sets the current board.

        Args:
            board: The current board.

        Returns:
            None.
        """
        self.board = board

    def getThisName(self) -> str:
            """Gets the name of the player.

            Args:
                None.

            Returns:
                A copy of the attribute name.

            """
            return self.thisName

    def getP1Name(self) -> str:
        """Gets the name of the player.

        Args:
            None.

        Returns:
            A copy of the attribute name.

        """
        return self.p1Name

    def getP2Name(self) -> str:
        """Gets the name of the player.

        Args:
            None.

        Returns:
            A copy of the attribute name.

        """
        return self.p2Name

    def getLastMove(self) -> str:
        """Gets the name of the player who last moved.

        Args:
            None.

        Returns:
            A copy of the attribute last_move.
        """
        return self.last_move

    def getNumWins(self) -> int:
        """Gets the total number of wins.

        Args:
            None.

        Returns:
            A copy of the attribute num_wins.
        """
        return self.num_wins

    def getNumTies(self) -> int:
        """Gets the total number of ties.

        Args:
            None.

        Returns:
            A copy of the attribute num_ties.
        """
        return self.num_ties

    def getNumLosses(self) -> int:
        """Gets the total number of losses.

        Args:
            None.

        Returns:
            A copy of the attribute num_losses.
        """
        return self.num_losses

    def getGamesPlayed(self) -> int:
        """Gets the total number of games played.

        Args:
            None.

        Returns:
            A copy of the attribute gamedPlayed.
        """
        return self.games_played

    def updateGamesPlayed(self) -> None:
        """Updates the number of games played by one.

        Args:
            None.

        Returns:
            None.
        """
        self.setGamesPlayed(self.getGamesPlayed() + 1)

    def resetGameBoard(self) -> None:
        """Resets the gameboard.

        Using the setBoard() function, this function will
        set the board to the default state. This function
        also sets the attribute last_move to "player2".

        Args:
            None.

        Returns:
            None.
        """
        self.setBoard([[" "," "," "],[" "," "," "],[" "," "," "]])
        self.setLastMove(self.p2Name)

    def updateGameBoard(self, row, col) -> None:
        """Updates the board with the corresponding row/col.

        If the attribute last_move equals "player2", the corresponding
        row and column of the board will equal "X". Otherwise, it would
        be "O".

        Args:
            row: row of the board.
            col: column of the board.

        Returns:
            None.
        """
        if self.getLastMove() == self.getP2Name():
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

    def isWinner(self) -> bool:
        """Checks if the current board contains a winning move.

        Checks current board twice, each time with token = "X" and token = "O"
        to see if any player has made a winning move. If a winning move is found,
        this function will increment attribute num_wins by 1 if the attribute name
        equals the attribute last_move. Otherwise, the attribute num_losses will
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
            if self.getThisName() == self.getLastMove():
                self.setNumWins(self.getNumWins() + 1)
            else:
                self.setNumLosses(self.getNumLosses() + 1)
            return True
        return False


    def boardIsFull(self) -> bool:
        """Checks if the current board is full.

        Loops through the current board and returns False if
        there is a space found (empty space). If no space is
        found, the attribute num_ties will be incremented by 1.

        Args:
            None.

        Returns:
            True: The board is full.
            False: The board is not full.
        """
        for row in self.board:
            if row.count(" ") != 0:
                return False
        self.setNumTies(self.getNumTies() + 1)
        return True

    def computeStats(self) -> tuple[str, str, int, int, int, int]:
        """Computes the final stats for the current player.

        This function will return player 1's name, player 2's name,
        total games played, and number of wins, losses, and ties.

        Args:
            None.

        Returns:
            None.
        """
        return self.p1Name, self.p2Name, self.games_played, self.num_wins, self.num_losses, self.num_ties